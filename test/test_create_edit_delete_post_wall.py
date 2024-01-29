import logging

from test.api.crud.like.like_crud import LikeCrud
from test.api.crud.user.user_crud import UserCrud
from test.api.crud.wall.wall_crud_comment import WallCrudComment
from test.api.crud.wall.wall_crud_photo import WallCrudPhoto
from test.api.crud.wall.wall_crud_post import WallCrudPost
from test.api.data.model.requests_model.request_comment_api import RequestCommentApi
from test.api.data.model.requests_model.request_delete_post import RequestDeletePost
from test.api.data.model.requests_model.request_edit_post_api import RequestEditPostApi
from test.api.data.model.requests_model.request_get_photo_url_api import RequestGetPhotoUrlApi
from test.api.data.model.requests_model.request_post_wall_api import RequestPostWallApi
from test.api.data.model.requests_model.request_post_wall_like import RequestPostWallLike
from test.api.data.model.requests_model.request_save_photo_to_server import RequestSavePhotoToServer
from test.api.data.model.requests_model.request_user_api import RequestUserApi
from test.api.data.model.response_model.response_get_photo_url_api import ResponseGetPhotoUrlApi
from test.api.data.model.response_model.response_like_from_post import ResponseLikeFromPost
from test.api.data.model.response_model.response_photo_api import ResponsePhotoApi
from test.api.data.model.response_model.response_post_wall_api import ResponsePostWallApi
from test.api.data.model.response_model.response_upload_file_to_server import ResponseUploadFileToServer
from test.api.data.model.response_model.response_user_api import ResponseUserApi
from test.api.data.path_to_file import PathToFile
from test.test.data_test.data_test_user import DataTestUser
from test.test.steps.get_url_photo_step import PhotoStep
from test.ui.pages.auth.registration_page import RegistrationPage
from test.ui.pages.my_page_page import MyPagePage
from test.ui.pages.news_page import NewsPage
from test.utils.utils import Utils

logger = logging.getLogger(__name__)


class TestCreateAndCheckRecordFromWall:

    def test_sign_up_and_upload_image(self, init_driver):
        """
        Тест: создание поста на стене ВК страницы,
        редактирование его, добавление фото,
        оставление реакции под постом,
        оставление комментария,
        проверка в процессе всех данных и удаление поста
        """
        # region Шаг 1: переход на главную страницу
        logger.info("Шаг 1: переход на страницу авторизации")

        registration_page = RegistrationPage()
        assert registration_page.state.is_displayed(), "Переход на страницу авторизации не совершен"
        # endregion

        # region Шаг 2: Ввод логина и пароля
        logger.info("Шаг 2: Ввод логина и пароля, переход на страницу новостей")

        registration_page.input_login_in_form(DataTestUser.USER_LOGIN)
        registration_page.click_button_sing_in()

        registration_page.password_form.state.wait_for_displayed()

        registration_page.password_form.input_password_in_form(DataTestUser.USER_PASSWORD)
        registration_page.password_form.click_button_continue()

        feed_page = NewsPage()
        feed_page.state.wait_for_displayed()

        assert feed_page.state.is_displayed(), "Страница новостей ВК не открыта"
        # endregion

        # region Шаг 3: переход на страницу "Моя страница"
        logger.info("Шаг 3: переход на страницу 'Моя страница'")

        feed_page.click_button_my_page()

        my_page_page = MyPagePage()
        my_page_page.state.wait_for_displayed()

        assert my_page_page.state.is_displayed(), "Страница 'Моя страница' ВК не открыта"
        # endregion

        # region Шаг 4: создание случайного текста на стене, проверка его наличие и автора на стене через UI
        logger.info("Шаг 4: создание случайного текста на стене, проверка его наличие и автора на стене через UI")

        random_text_for_post = Utils.random_text()

        params_from_post_wall = RequestPostWallApi(message=random_text_for_post).to_dict()
        response_create_post = WallCrudPost().create_post_from_wall(params=params_from_post_wall).json()

        post_id_response = ResponsePostWallApi.from_dict(response_create_post["response"])

        post_id_api = post_id_response.post_id

        text_from_record = my_page_page.get_text_from_record_wall(user_id=DataTestUser.USER_ID,
                                                                  post_id=post_id_api)

        param_from_user_name = RequestUserApi(user_ids=DataTestUser.USER_ID).to_dict()
        response_from_user = UserCrud().get_user_by_id(params=param_from_user_name).json()

        response_user_api = ResponseUserApi.from_dict(response_from_user['response'][0])

        full_name = f'{response_user_api.first_name} {response_user_api.last_name}'

        assert (
                full_name in text_from_record
                and random_text_for_post in text_from_record
        ), f"Запись на стене сделана от неправильного пользователя, текст не соответствует ожидаемому"
        # endregion

        # region Шаг 5: редактируем запись и добавляем картинку. Проверяем корректность данных
        logger.info("Шаг 5: редактируем запись и добавляем картинку. Проверяем корректность данных")

        params_from_url_upload = RequestGetPhotoUrlApi()
        response_url_photo = WallCrudPhoto().get_address_from_upload_photo(
            params=params_from_url_upload.to_dict()).json()

        upload_photo_api = ResponseGetPhotoUrlApi.from_dict(response_url_photo["response"])
        upload_server = upload_photo_api.upload_url

        path_to_file = PathToFile.PATH_TO_PHOTO
        upload_file_to_server = WallCrudPhoto().get_upload_file_to_server(
            upload_server=upload_server, upload_files={'photo': open(path_to_file, 'rb')}).json()

        response_upload_file = ResponseUploadFileToServer.from_dict(upload_file_to_server)

        server = response_upload_file.server
        photo = response_upload_file.photo
        hash_photo = response_upload_file.hash

        param_photo_upload = RequestSavePhotoToServer(server=server, photo=photo, hash=hash_photo)
        save_photo_to_server = WallCrudPhoto().save_wall_photo(params=param_photo_upload.to_dict()).json()

        photo_api = ResponsePhotoApi.from_dict(save_photo_to_server['response'][0])
        photo_id = photo_api.id

        new_text = Utils.random_text()

        params_post_edit = RequestEditPostApi(
            post_id=post_id_api,
            message=new_text,
            attachments=str(RequestEditPostApi.attachments_post_api(photo_id=photo_id, user_id=DataTestUser.USER_ID)))
        WallCrudPost().edit_post_from_wall(params_post_edit.to_dict())

        my_page_page.wait_text_post_on_display(
            post_id=post_id_api,
            user_id=DataTestUser.USER_ID,
            text=new_text
        )

        new_text_from_record = my_page_page.get_text_from_record_wall(user_id=DataTestUser.USER_ID,
                                                                      post_id=post_id_api)

        url_picture_api = PhotoStep.url_photo_from_wall()
        Utils.download_photo(url=url_picture_api, path=PathToFile.PATH_TO_PHOTO_DOWNLOAD)

        assert new_text in new_text_from_record, f"Текст записи post: {post_id_api} на стене не изменился"

        assert my_page_page.check_picture_on_display(DataTestUser.USER_ID, photo_id), \
            f"Картинка не добавилась в post: {post_id_api} на стене"

        assert Utils.compare_images(PathToFile.PATH_TO_PHOTO, PathToFile.PATH_TO_PHOTO_DOWNLOAD), \
            "Картинка на стене не соответствует загружаемой картинке."
        # endregion

        # region Шаг 6: добавляем комментарий к записи на стене. Проверяем корректность данных
        logger.info("Шаг 6: добавляем комментарий к записи на стене. Проверяем корректность данных")

        random_text_from_comment = Utils.random_text()

        param_from_create_comment = RequestCommentApi(post_id=post_id_api, message=random_text_from_comment)
        WallCrudComment().create_comment(params=param_from_create_comment.to_dict())

        my_page_page.click_to_open_comments()

        my_page_page.wait_text_comment_on_display(random_text_from_comment)

        text_author_from_first_comment = my_page_page.get_wall_first_comment_post_text(user_id=DataTestUser.USER_ID,
                                                                                       post_id=post_id_api)

        assert full_name in text_author_from_first_comment, "Комментарий сделан от неправильного пользователя"
        assert random_text_from_comment in text_author_from_first_comment, f"Комментарий содержит не верную информацию"
        # endregion

        # region Шаг 7: ставим лайк. Проверяем корректность данных
        logger.info("Шаг 7: ставим лайк. Проверяем корректность данных")

        my_page_page.click_to_like_for_first_record(post_id_api)

        my_page_page.wait_like_to_display(post_id=post_id_api, user_id=DataTestUser.USER_ID)

        params_get_like = RequestPostWallLike(item_id=post_id_api)
        people_who_like = LikeCrud().get_likes(params=params_get_like.to_dict()).json()

        response_like_post = ResponseLikeFromPost.from_dict(people_who_like['response'])
        id_people_who_like = response_like_post.items[0].id

        assert int(DataTestUser.USER_ID) == id_people_who_like, 'Юзер поставивший лайк не совпадает с ожидаемым'
        # endregion

        # region Шаг 8: удаляем запись со стены. Проверяем корректность удаления
        logger.info("Шаг 8: удаляем запись со стены. Проверяем корректность удаления")

        param_for_delete_post = RequestDeletePost(post_id_api)

        WallCrudPost().delete_post_from_wall(params=param_for_delete_post.to_dict())

        assert my_page_page.check_delete_post_from_wall(DataTestUser.USER_ID, photo_id), 'Пост не удалился'
        # endregion

from test.api.crud.wall.wall_crud_post import WallCrudPost
from test.api.data.model.requests_model.pre_base_model import PreBase


class PhotoStep:

    @staticmethod
    def url_photo_from_wall():
        params_fo_get = PreBase()
        response_post_on_wall = WallCrudPost().get_post_from_wall(params=params_fo_get.to_dict()).json()
        response_dict = response_post_on_wall['response']['items'][0]['attachments'][0]['photo']['sizes']
        return max(response_dict, key=lambda d: d['width'])['url']

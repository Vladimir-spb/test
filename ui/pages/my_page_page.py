from py_selenium_auto.elements.text_box import TextBox
from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from selenium.webdriver.common.by import By


class MyPagePage(Form):

    def __init__(self):
        super().__init__(
            Locator(By.XPATH, "//*[contains(@id,'profile_redesigned')]"),
            "My page")

        self.__button_open_comments = self._element_factory.get_text_box(
            Locator(By.XPATH, f"//*[contains(@class,'js-replies_next_label')]"),
            "Open comments"
        )

    def get_text_from_record_wall(self, user_id, post_id):
        elem = self._element_factory.get(
            TextBox,
            Locator(By.XPATH, f"//*[contains(@id,'post{user_id}_{post_id}')]"),
            "Text from record"
        )
        return elem.text

    def check_picture_on_display(self, user_id, picture_id):
        return self._element_factory.get(
            TextBox,
            Locator(By.XPATH, f"//a[contains(@href,'/photo{user_id}_{picture_id}')]"),
            "Picture on wall"
        ).state.is_displayed()

    def get_wall_first_comment_post_text(self, user_id, post_id):
        return self._element_factory.get_text_box(
            Locator(By.XPATH,
                    f"//*[contains(@id,'replies{user_id}_{post_id}')]"),
            "Text from comment"
        ).text

    def click_to_like_for_first_record(self, post_id):
        self._element_factory.get_text_box(
            Locator(By.XPATH,
                    f"//*[contains(@class,'PostBottomActionContainer')]"
                    f"/div[contains(@data-reaction-target-object,'{post_id}')]"),
            "Like button for record from wall my page"
        ).wait_and_click()

    def click_to_open_comments(self):
        self.__button_open_comments.click()

    def wait_text_comment_on_display(self, text):
        return self._element_factory.get(
            TextBox,
            Locator(By.XPATH, f"//*[contains(@class,'wall_reply_text') and contains(text(),'{text}')]"),
            "Wait text comment"
        ).state.wait_for_displayed()

    def wait_text_post_on_display(self, text, user_id, post_id):
        return self._element_factory.get(
            TextBox,
            Locator(By.XPATH, f"//*[contains(@id,'wpt{user_id}_{post_id}') and contains(text(),'{text}')]"),
            "Wait text post"
        ).state.wait_for_displayed()

    def wait_like_to_display(self, user_id, post_id, count_like=1):
        return self._element_factory.get(
            TextBox,
            Locator(By.XPATH, f"//*[contains(@data-reaction-target-object,'wall{user_id}_{post_id}')"
                              f" and contains(@data-reaction-counts,'{count_like}')]"),
            "Wait like post"
        ).state.wait_for_displayed()

    def check_delete_post_from_wall(self, user_id, post_id):
        return self._element_factory.get(
            TextBox,
            Locator(By.XPATH, f"//*[contains(@id,'post{user_id}_{post_id}')]"),
            "Wait post delete"
        ).state.wait_for_not_displayed()

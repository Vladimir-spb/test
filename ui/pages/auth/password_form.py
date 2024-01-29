from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from selenium.webdriver.common.by import By


class PasswordForm(Form):

    def __init__(self):
        super().__init__(
            Locator(By.XPATH, "//form[contains(@class,'EnterPasswordNoUserInfo')]"),
            "Password form")

        self.__password_field = self._element_factory.get_text_box(
            Locator(By.XPATH, "//input[contains(@name,'password')]"),
            "Password field"
        )

        self.__button_continue = self._element_factory.get_button(
            Locator(By.XPATH, "//button[contains(@type,'submit')]"),
            "Sing in button"
        )

    def input_password_in_form(self, password: str):
        self.__password_field.clear_and_type(password)

    def click_button_continue(self):
        self.__button_continue.wait_and_click()

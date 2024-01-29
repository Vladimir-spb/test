from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from selenium.webdriver.common.by import By

from ui.pages.auth.password_form import PasswordForm


class RegistrationPage(Form):
    def __init__(self):
        super().__init__(
            Locator(By.XPATH, "//form[contains(@class,'VkIdForm')]"),
            "Registration Page")

        self.password_form = PasswordForm()

        self.__login_field = self._element_factory.get_text_box(
            Locator(By.XPATH, "//input[contains(@name,'login')]"),
            "Login field"
        )

        self.__button_sign_in = self._element_factory.get_button(
            Locator(By.XPATH, "//button[contains(@class,'signInButton')]"),
            "Sing in button"
        )

    def input_login_in_form(self, login: str):
        self.__login_field.clear_and_type(login)

    def click_button_sing_in(self):
        self.__button_sign_in.wait_and_click()

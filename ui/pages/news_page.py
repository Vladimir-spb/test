from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from selenium.webdriver.common.by import By


class NewsPage(Form):

    def __init__(self):
        super().__init__(
            Locator(By.XPATH, "//*[contains(@id,'main_feed')]"),
            "Feed Page")

        self.__my_page_button = self._element_factory.get_text_box(
            Locator(By.XPATH, "//li[contains(@id,'l_pr')]"),
            "My page button"
        )

    def click_button_my_page(self):
        self.__my_page_button.wait_and_click()

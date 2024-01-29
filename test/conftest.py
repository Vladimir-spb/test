import os

import pytest
from py_selenium_auto.browsers.browser_services import BrowserServices
from py_selenium_auto_core.utilities.root_path_helper import RootPathHelper

from ui.data.url_manager_ui import UrlManagerUi


@pytest.fixture(scope="session", autouse=True)
def setup_session(request):
    # TODO: workaround to set calling root path, because pytest runs from the root dir
    work_dir = RootPathHelper.current_root_path(__file__)
    os.chdir(work_dir)


@pytest.fixture()
def init_driver():
    browser = BrowserServices.Instance.browser
    browser.maximize()
    BrowserServices.Instance.browser.go_to(UrlManagerUi.URL_UI)

    yield

    browser.quit()

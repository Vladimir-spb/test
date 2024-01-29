import requests

from test.api.data.url_manager_api import UrlManagerApi


class BaseCrud:
    def __init__(self, method: str):
        self.method = method

    def request_vk_api(self, submethod, params):
        return requests.get(f"{UrlManagerApi.URL_API}{self.method}.{submethod}", params=params)

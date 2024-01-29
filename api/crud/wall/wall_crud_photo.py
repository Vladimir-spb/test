import requests

from api.crud.base_crud.base_crud import BaseCrud


class WallCrudPhoto(BaseCrud):
    def __init__(self):
        super().__init__('photos')

    def get_address_from_upload_photo(self, params):
        submethod = 'getWallUploadServer'
        return self.request_vk_api(submethod, params)

    def save_wall_photo(self, params):
        submethod = 'saveWallPhoto'
        return self.request_vk_api(submethod, params)

    def get_upload_file_to_server(self, upload_server, upload_files):
        return requests.post(upload_server, files=upload_files)

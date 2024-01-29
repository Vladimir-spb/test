from api.crud.base_crud.base_crud import BaseCrud


class UserCrud(BaseCrud):
    def __init__(self):
        super().__init__('users')

    def get_user_by_id(self, params):
        submethod = 'get'
        return self.request_vk_api(submethod, params)

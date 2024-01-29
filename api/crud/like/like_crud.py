from api.crud.base_crud.base_crud import BaseCrud


class LikeCrud(BaseCrud):
    def __init__(self):
        super().__init__('likes')

    def get_likes(self, params):
        submethod = 'getList'
        return self.request_vk_api(submethod, params)

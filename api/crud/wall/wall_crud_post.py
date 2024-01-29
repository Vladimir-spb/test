from test.api.crud.base_crud.base_crud import BaseCrud


class WallCrudPost(BaseCrud):
    def __init__(self):
        super().__init__('wall')

    def get_post_from_wall(self, params):
        submethod = 'get'
        return self.request_vk_api(submethod, params)

    def create_post_from_wall(self, params):
        submethod = 'post'
        return self.request_vk_api(submethod, params)

    def get_post_wall_by_id(self, params):
        submethod = 'getById'
        return self.request_vk_api(submethod, params)

    def edit_post_from_wall(self, params):
        submethod = 'edit'
        return self.request_vk_api(submethod, params)

    def delete_post_from_wall(self, params):
        submethod = 'delete'
        return self.request_vk_api(submethod, params)

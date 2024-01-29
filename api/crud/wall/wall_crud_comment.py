from test.api.crud.wall.wall_crud_post import WallCrudPost


class WallCrudComment(WallCrudPost):

    def create_comment(self, params):
        submethod = 'createComment'
        return self.request_vk_api(submethod, params)

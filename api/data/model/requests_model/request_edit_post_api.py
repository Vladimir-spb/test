from dataclasses import dataclass

from api.data.model.requests_model.pre_base_model import PreBase


@dataclass
class RequestEditPostApi(PreBase):
    post_id: int = None
    message: str = None
    attachments: str = None

    @staticmethod
    def attachments_post_api(user_id, photo_id, type_item='photo', ):
        return f'{type_item}{user_id}_{photo_id}'

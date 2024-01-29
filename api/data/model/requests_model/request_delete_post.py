from dataclasses import dataclass

from api.data.model.requests_model.pre_base_model import PreBase


@dataclass
class RequestDeletePost(PreBase):
    post_id: int = None

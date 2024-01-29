from dataclasses import dataclass

from test.api.data.model.requests_model.pre_base_model import PreBase


@dataclass
class RequestCommentApi(PreBase):
    post_id: int = None
    message: str = None

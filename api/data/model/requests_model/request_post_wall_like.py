from dataclasses import dataclass

from api.data.model.requests_model.pre_base_model import PreBase


@dataclass
class RequestPostWallLike(PreBase):
    type: str = 'post'
    item_id: int = None
    extended: bool = True

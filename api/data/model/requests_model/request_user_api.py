from dataclasses import dataclass

from api.data.model.requests_model.pre_base_model import PreBase


@dataclass
class RequestUserApi(PreBase):
    user_ids: int = None

from dataclasses import dataclass

from test.api.data.model.requests_model.pre_base_model import PreBase


@dataclass
class RequestSavePhotoToServer(PreBase):
    server: int = None
    photo: str = None
    hash: str = None

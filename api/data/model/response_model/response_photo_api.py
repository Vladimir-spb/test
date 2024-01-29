from dataclasses import dataclass
from typing import List

from dataclasses_json import DataClassJsonMixin, dataclass_json


@dataclass_json
@dataclass
class Sizes(DataClassJsonMixin):
    height: int
    type: str
    width: int
    url: str


@dataclass_json
@dataclass
class ResponsePhotoApi(DataClassJsonMixin):
    album_id: int
    date: int
    id: int
    owner_id: int
    access_key: str
    sizes: List[Sizes]
    text: str
    web_view_token: str
    has_tags: bool

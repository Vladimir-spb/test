from dataclasses import dataclass
from typing import List

from dataclasses_json import DataClassJsonMixin, dataclass_json


@dataclass_json
@dataclass
class Items(DataClassJsonMixin):
    can_access_closed: bool
    first_name: str
    id: int
    is_closed: bool
    last_name: str
    type: str


@dataclass_json
@dataclass
class ResponseLikeFromPost(DataClassJsonMixin):
    count: int
    items: List[Items]
    reactions: List[int]
    reaction_set_id: str
    reaction_sets: List[dict]

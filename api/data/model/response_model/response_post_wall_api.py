from dataclasses import dataclass

from dataclasses_json import DataClassJsonMixin, dataclass_json


@dataclass_json
@dataclass
class ResponsePostWallApi(DataClassJsonMixin):
    post_id: int

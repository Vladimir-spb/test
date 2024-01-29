from dataclasses import dataclass

from dataclasses_json import DataClassJsonMixin, dataclass_json


@dataclass_json
@dataclass
class ResponseUserApi(DataClassJsonMixin):
    first_name: str
    last_name: str
    can_access_closed: bool
    is_closed: bool

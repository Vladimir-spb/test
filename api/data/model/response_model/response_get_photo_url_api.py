from dataclasses import dataclass

from dataclasses_json import DataClassJsonMixin, dataclass_json


@dataclass_json
@dataclass
class ResponseGetPhotoUrlApi(DataClassJsonMixin):
    album_id: int
    upload_url: str
    user_id: int

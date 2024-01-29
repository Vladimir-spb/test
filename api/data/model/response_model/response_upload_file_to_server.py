from dataclasses import dataclass

from dataclasses_json import DataClassJsonMixin, dataclass_json


@dataclass_json
@dataclass
class ResponseUploadFileToServer(DataClassJsonMixin):
    server: int
    photo: str
    hash: str

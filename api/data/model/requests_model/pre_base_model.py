from dataclasses import dataclass

from dataclasses_json import DataClassJsonMixin

from test.test.data_test.data_test_user import DataTestUser


@dataclass
class PreBase(DataClassJsonMixin):
    access_token: str = DataTestUser.ACCESS_TOKEN
    v: str = DataTestUser.VERSION_API

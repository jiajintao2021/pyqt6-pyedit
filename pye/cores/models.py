import typing

from pydantic import BaseModel


class SettingsModel(BaseModel):
    project: typing.List[typing.Optional[str]] = []

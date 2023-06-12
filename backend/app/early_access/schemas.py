import datetime
import re
import typing

from pydantic import BaseModel, validator


class PostRequest(BaseModel):
    email: str = "mr.pipiskin228@mail.ru"
    type: typing.Optional[str] = "main"

    @validator("email")
    def email_valifator(
            cls: typing.Any,
            email: str,
    ) -> typing.Union[ValueError, str]:
        email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        total_chars = len(email)
        if not email_regex.match(email):
            raise ValueError("E-mail not valid")
        if total_chars > 256:
            raise ValueError("E-mail cannot be longer than 256 characters")
        if total_chars < 5:
            raise ValueError("E-mail is too short")
        return email


class PostResponse(BaseModel):
    id: int = 1
    email: str = "mr.pipiskin228@mail.ru"
    type: str = "main"
    status: str = "waiting"
    created_at: datetime.datetime = datetime.datetime.now()

    class Config:
        orm_mode=True


class GetResponse(BaseModel):
    count: int = 1
    items: typing.List[PostResponse]

    class Config:
        orm_mode=True


class PatchRequest(BaseModel):
    id: int = 1
    status: str = "accepted"

    @validator("status")
    def status_validator(
            cls: typing.Any,
            status: str,
    ) -> typing.Union[ValueError, str]:
        statuses = re.compile(r"\b(waiting|accepted|rejected)\b")
        if not statuses.match(status):
            raise ValueError(f"Status has an undefined state ({status})")
        return status

class PatchResponse(BaseModel):
    id: int = 1
    email: str = "mr.pipiskin228@mail.ru"
    type: str = "main"
    status: str = "accepted"
    created_at: datetime.datetime

    class Config:
        orm_mode=True

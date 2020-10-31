from dataclasses import dataclass
from datetime import datetime
from enum import Enum, IntEnum
from typing import Optional, Sequence
from uuid import UUID
from pydantic import BaseModel


class CatType(Enum):
    EUROPEAN = "european"
    PERSIAN = "persian"


class Foo(IntEnum):
    FOO = 1
    UFO = 2


class SomethingElse(BaseModel):
    name: str
    active: bool
    type: CatType
    foo: Foo


@dataclass
class CreateCatInput:
    name: str
    active: bool
    type: CatType
    foo: Foo


@dataclass
class CreateCatOutput:
    id: UUID


@dataclass
class FriendInput:
    id: str
    best: bool


@dataclass
class Cat:
    id: UUID
    name: str
    active: bool
    type: CatType
    foo: Foo
    creation_time: datetime
    friends: Sequence["Cat"]


@dataclass
class UpdateCatInput:
    name: str
    active: bool
    friends: Optional[Sequence[FriendInput]]


@dataclass
class HttpError:
    status: int
    message: str
    code: str

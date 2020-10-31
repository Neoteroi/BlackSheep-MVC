from dataclasses import dataclass
from datetime import datetime
from enum import Enum, IntEnum
from typing import List
from uuid import UUID


class CatType(Enum):
    EUROPEAN = "european"
    PERSIAN = "persian"


class Foo(IntEnum):
    FOO = 1
    UFO = 2


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
    creation_time: datetime


@dataclass
class UpdateCatInput:
    name: str
    active: bool


@dataclass
class HttpError:
    status: int
    message: str
    code: str


@dataclass
class CatsList:
    items: List[Cat]
    total: int

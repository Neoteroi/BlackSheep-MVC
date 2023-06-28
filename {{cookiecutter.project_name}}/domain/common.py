"""
Common domain models reused across several API endpoints.
"""
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Generic, TypeVar

from pydantic import BaseModel, Field, conint

T = TypeVar("T")


@dataclass(slots=True)
class PaginatedSet(Generic[T]):
    items: list[T]
    total: int

    def __iter__(self):
        yield from self.items

    def __len__(self) -> int:
        return len(self.items)


@dataclass(slots=True)
class SetterAction(Generic[T]):
    """
    Describes an action that requires adding and removing objects from a collection.
    """

    add: list[T] = field(default_factory=list)
    remove: list[T] = field(default_factory=list)


class SortOrder(Enum):
    ASC = "ASC"
    DESC = "DESC"


class PageOptions(BaseModel):
    """
    Common pagination options for all endpoints implementing pagination of
    results.

    - page, for page number
    - limit, for results per page
    - continuation_id, the last numeric ID that was read
    """

    page: conint(gt=0) = Field(1, description="Page number.")  # type: ignore
    limit: conint(gt=0, le=1000) = Field(  # type: ignore
        100, description="Maximum number of results per page."
    )
    continuation_id: int | None = Field(
        None, description="If provided, the ID of the last object that was retrieved."
    )
    sort_order: SortOrder = SortOrder.ASC


class TimedMixin(BaseModel):
    created_at: datetime
    updated_at: datetime
    etag: str

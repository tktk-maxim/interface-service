import strawberry
from typing import Optional
from datetime import date


@strawberry.type
class Event:
    id: int
    employee: int
    begin: date
    end: date
    description: Optional[str]


@strawberry.input
class EventInput:
    employee: int
    begin: date
    end: date
    description: Optional[str]


@strawberry.type
class EventForCard:
    begin: date
    end: date
    description: Optional[str]



import strawberry
from typing import Optional
from datetime import date


@strawberry.type
class Event:
    id: int
    employee_id: int
    begin: str
    end: str
    description: Optional[str] = ""


@strawberry.input
class EventInput:
    employee_id: int
    begin: str
    end: str
    description: Optional[str] = ""


@strawberry.type
class EventForCard:
    begin: str
    end: str
    description: Optional[str] = ""



import strawberry
from typing import Optional, List
from schemas.event import EventForCard


@strawberry.type
class Employee:
    id: int
    first_name: str
    last_name: str
    middle_name: Optional[str] = ""
    login: str
    password: str
    email: str
    subdivision_id: int
    leader: Optional[bool] = False
    chat_id: int | None = 0
    telegram_name: str


@strawberry.input
class EmployeeInput:
    first_name: str
    last_name: str
    middle_name: Optional[str] = ""
    login: str
    password: str
    email: str
    subdivision_id: int
    leader: Optional[bool] = False
    chat_id: int | None = 0
    telegram_name: str


@strawberry.input
class SearchEmployeeInput:
    first_name: Optional[str] = ""
    last_name: Optional[str] = ""
    middle_name: Optional[str] = None
    login: Optional[str] = ""
    email: Optional[str] = ""
    telegram_name: Optional[str] = ""


@strawberry.type
class EmployeeCard:
    employee: Employee
    events: List[EventForCard]

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


@strawberry.input
class SearchEmployeeInput:
    first_name: Optional[str] = ""
    last_name: Optional[str] = ""
    middle_name: Optional[str] = None
    login: Optional[str] = ""
    email: Optional[str] = ""


@strawberry.type
class EmployeeCard:
    employee: Employee
    events: List[EventForCard]

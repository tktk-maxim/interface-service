import strawberry
from typing import Optional


@strawberry.type
class Employee:
    id: int
    first_name: str
    last_name: str
    middle_name: Optional[str]
    login: str
    password: str
    email: str
    subdivision: int
    leader: Optional[bool]


@strawberry.input
class EmployeeInput:
    first_name: str
    last_name: str
    middle_name: Optional[str]
    login: str
    password: str
    email: str
    subdivision: int
    leader: Optional[bool]

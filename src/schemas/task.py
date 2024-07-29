from typing import Optional

import strawberry


@strawberry.type
class Task:
    id: int
    name: str
    description: str
    estimated_days_to_complete: int
    actual_days_to_complete: Optional[int] = None
    hours_spent: Optional[int] = 0
    employee_id: Optional[int] = None
    done: bool | Optional[bool] = False
    project_id: int


@strawberry.input
class TaskInput:
    name: str
    description: str
    estimated_days_to_complete: int
    actual_days_to_complete: Optional[int] = None
    hours_spent: Optional[int] = 0
    employee_id: Optional[int] = None
    done: bool | Optional[bool] = False
    project_id: int


@strawberry.input
class SearchTaskInput:
    name: Optional[str] = ""
    description: Optional[str] = ""
    estimated_days_to_complete: Optional[int] = ""
    actual_days_to_complete: Optional[int] = None
    hours_spent: Optional[int] = 0
    employee_id: Optional[int] = None
    done: bool | Optional[bool] = False
    project_id: Optional[int] = ""


@strawberry.input
class TaskFilterInput:
    employee_id: int
    more_days_to_complete: Optional[int] = None
    less_days_to_complete: Optional[int] = None
    done: Optional[bool] = None
    project_id: Optional[int] = None


@strawberry.input
class TaskSortInput:
    name: Optional[bool] = None
    description: Optional[bool] = None
    estimated_days_to_complete: Optional[bool] = None
    actual_days_to_complete: Optional[bool] = None
    hours_spent: Optional[bool] = None
    employee_id: Optional[bool] = None
    done: Optional[bool] = None
    project_id: Optional[bool] = None

from typing import Optional

import strawberry


@strawberry.type
class Task:
    id: int
    name: str
    description: str
    time_complete_in_days: int
    project_id: int


@strawberry.input
class TaskInput:
    name: str
    description: str
    time_complete_in_days: Optional[int] = None
    project_id: int


@strawberry.input
class SearchTaskInput:
    name: Optional[str] = ""
    description: Optional[str] = ""
    time_complete_in_days: Optional[int] = None
    project_id: Optional[int] = ""


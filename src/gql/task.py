import strawberry
from typing import List, AsyncGenerator, Optional
from resolvers.task import (get_task, get_tasks, create_task_view,
                            update_task_view, delete_task_view, search_task_view)
from schemas.task import Task


@strawberry.type
class Query:
    task: Task = strawberry.field(resolver=get_task)
    tasks: List[Task] = strawberry.field(resolver=get_tasks)
    search_task: List[Task] = strawberry.field(resolver=search_task_view)


@strawberry.type
class Mutation:
    create_task: Task = strawberry.mutation(resolver=create_task_view)
    update_task: Task = strawberry.mutation(resolver=update_task_view)
    delete_task: str = strawberry.mutation(resolver=delete_task_view)

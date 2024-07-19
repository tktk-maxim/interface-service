import strawberry
from typing import List, AsyncGenerator, Optional
from crud import get_obj, create_obj, update_obj, delete_obj
from schemas.task import Task, TaskInput, SearchTaskInput
from config import settings


async def get_task(task_id: int) -> Optional[Task]:
    task_data = await get_obj(f"http://{settings.task_service_host}:{settings.task_service_port}"
                              f"/task/{task_id}")
    return Task(**task_data)


async def get_tasks() -> List[Task]:
    tasks = await get_obj(f"http://{settings.task_service_host}:{settings.task_service_port}"
                          f"/task/all/")
    return [Task(**task) for task in tasks]


async def create_task_view(task: TaskInput) -> Optional[Task]:
    task_data = await create_obj(f"http://{settings.task_service_host}:{settings.task_service_port}"
                                 f"/create/",
                                 data=task.__dict__)
    return Task(**task_data)


async def search_task_view(task: SearchTaskInput) -> List[Task]:
    tasks = await get_obj(f"http://{settings.task_service_host}:{settings.task_service_port}"
                          f"/task/search/?name={task.name}"
                          f"&description={task.description}&project_id={task.project_id}")
    return [Task(**task) for task in tasks]


async def update_task_view(task_id: int, task: TaskInput) -> Optional[Task]:
    task_data = await update_obj(f"http://{settings.task_service_host}:{settings.task_service_port}"
                                 f"/task/{task_id}",
                                 data=task.__dict__)
    return Task(**task_data)


async def delete_task_view(task_id: int) -> str:
    task_data = await delete_obj(f"http://{settings.task_service_host}:{settings.task_service_port}"
                                 f"/task/{task_id}")
    return f'Deleted is {task_data["deleted"]}'

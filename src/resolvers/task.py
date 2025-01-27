import strawberry
from typing import List, AsyncGenerator, Optional
from crud import get_obj, create_obj, update_obj, delete_obj, update_obj_param
from schemas.task import Task, TaskInput, SearchTaskInput, TaskFilterInput, TaskSortInput
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
                                 f"/task/create/",
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


async def assign_task_employee_view(task_id: int, employee_id: int) -> Optional[Task]:
    task_data = await update_obj_param(f"http://{settings.task_service_host}:{settings.task_service_port}"
                                       f"/task/{task_id}", data={"employee_id": employee_id})
    return Task(**task_data)


async def add_hours_spent_view(task_id: int, hours: int) -> Optional[Task]:
    task_data = await update_obj_param(f"http://{settings.task_service_host}:{settings.task_service_port}"
                                       f"/task/add_hours/{task_id}?hours={hours}", data={})
    return Task(**task_data)


async def filter_tasks_view(filter_param: TaskFilterInput):
    url = ""
    for key, value in filter_param.__dict__.items():
        if value is not None:
            url += f"&{str(key)}={value}"

    tasks = await get_obj(f"http://{settings.task_service_host}:{settings.task_service_port}"
                          f"/task/filter/?" + url)
    return [Task(**task) for task in tasks]


async def sort_tasks_view(sort_param: TaskSortInput):
    url = ""
    for key, value in sort_param.__dict__.items():
        if value is not None:
            url += f"&{str(key)}={value}"

    tasks = await get_obj(f"http://{settings.task_service_host}:{settings.task_service_port}"
                          f"/task/sort/?" + url)
    return [Task(**task) for task in tasks]

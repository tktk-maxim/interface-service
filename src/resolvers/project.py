import strawberry
from typing import List, AsyncGenerator, Optional
from crud import get_obj, create_obj, update_obj, delete_obj
from schemas.project import Project, ProjectInput
from config import settings


async def get_project(project_id: int) -> Optional[Project]:
    project_data = await get_obj(f"http://{settings.task_service_host}:{settings.task_service_port}"
                                 f"/project/{project_id}")
    return Project(**project_data)


async def get_projects() -> List[Project]:
    projects = await get_obj(f"http://{settings.task_service_host}:{settings.task_service_port}"
                             f"/project/all/")
    return [Project(**project) for project in projects]


async def create_project_view(project: ProjectInput) -> Optional[Project]:
    project_data = await create_obj(f"http://{settings.task_service_host}:{settings.task_service_port}"
                                    f"/project/create/",
                                    data=project.__dict__)
    return Project(**project_data)


async def update_project_view(project_id: int, project: ProjectInput) -> Optional[Project]:
    project_data = await update_obj(f"http://{settings.task_service_host}:{settings.task_service_port}"
                                    f"/project/{project_id}",
                                    data=project.__dict__)
    return Project(**project_data)


async def delete_project_view(project_id: int) -> str:
    project_data = await delete_obj(f"http://{settings.task_service_host}:{settings.task_service_port}"
                                    f"/project/{project_id}")
    return f'Deleted is {project_data["deleted"]}'

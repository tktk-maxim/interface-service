import strawberry
from typing import List, Optional
from crud import get_obj, create_obj, update_obj, delete_obj
from schemas.subdivision import Subdivision, SubdivisionInput
from config import settings


async def get_subdivision(subdivision_id: int) -> Optional[Subdivision]:
    subdivision_data = await get_obj(f"http://{settings.user_service_host}:{settings.user_service_port}"
                                     f"/subdivision/{subdivision_id}")
    return Subdivision(**subdivision_data)


async def get_subdivisions() -> List[Subdivision]:
    subdivisions = await get_obj(f"http://{settings.user_service_host}:{settings.user_service_port}"
                                 f"/subdivision/all/")
    return [Subdivision(**subdivision) for subdivision in subdivisions]


async def create_subdivision_view(subdivision: SubdivisionInput) -> Optional[Subdivision]:
    subdivision_data = await create_obj(f"http://{settings.user_service_host}:{settings.user_service_port}"
                                        f"/subdivision/create/",
                                        data=subdivision.__dict__)
    return Subdivision(**subdivision_data)


async def update_subdivision_view(subdivision_id: int, subdivision: SubdivisionInput) -> Optional[Subdivision]:
    subdivision_data = await update_obj(f"http://{settings.user_service_host}:{settings.user_service_port}"
                                        f"/subdivision/{subdivision_id}",
                                        data=subdivision.__dict__)
    return Subdivision(**subdivision_data)


async def delete_subdivision_view(subdivision_id: int) -> str:
    subdivision_data = await delete_obj(f"http://{settings.user_service_host}:{settings.user_service_port}"
                                        f"/subdivision/{subdivision_id}")
    return f'Deleted is {subdivision_data["deleted"]}'

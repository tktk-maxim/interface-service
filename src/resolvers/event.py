import strawberry
from typing import List, Optional
from crud import get_obj, create_obj, update_obj, delete_obj
from schemas.event import Event, EventInput
from config import settings


async def get_event(event_id: int) -> Optional[Event]:
    event_data = await get_obj(f"http://{settings.user_service_host}:{settings.user_service_port}"
                               f"/event/{event_id}")
    return Event(**event_data)


async def get_events() -> List[Event]:
    events = await get_obj(f"http://{settings.user_service_host}:{settings.user_service_port}"
                           f"/event/all/")
    return [Event(**event) for event in events]


async def create_event_view(event: EventInput) -> Optional[Event]:
    print(event)
    event_data = await create_obj(f"http://{settings.user_service_host}:{settings.user_service_port}"
                                  f"/event/create/", data=event.__dict__)

    return Event(**event_data)


async def update_event_view(event_id: int, event: EventInput) -> Optional[Event]:
    event_data = await update_obj(f"http://{settings.user_service_host}:{settings.user_service_port}"
                                  f"/event/{event_id}", data=event.__dict__)
    return Event(**event_data)


async def delete_event_view(event_id: int) -> str:
    event_data = await delete_obj(f"http://{settings.user_service_host}:{settings.user_service_port}"
                                  f"/event/{event_id}")
    return f'Deleted is {event_data["deleted"]}'

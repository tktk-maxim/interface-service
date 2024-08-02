import strawberry
from typing import List, Optional
from resolvers.event import (get_event, get_events, create_event_view,
                             update_event_view, delete_event_view)
from schemas.event import Event
from auth.middleware import IsAuthenticated


@strawberry.type
class Query:
    event: Event = strawberry.field(resolver=get_event, permission_classes=[IsAuthenticated])
    events: List[Event] = strawberry.field(resolver=get_events, permission_classes=[IsAuthenticated])


@strawberry.type
class Mutation:
    create_event: Event = strawberry.mutation(resolver=create_event_view,
                                              permission_classes=[IsAuthenticated])

    update_event: Event = strawberry.mutation(resolver=update_event_view,
                                              permission_classes=[IsAuthenticated])

    delete_event: str = strawberry.mutation(resolver=delete_event_view,
                                            permission_classes=[IsAuthenticated])

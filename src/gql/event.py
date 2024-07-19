import strawberry
from typing import List, Optional
from resolvers.event import (get_event, get_events, create_event_view,
                             update_event_view, delete_event_view)
from schemas.event import Event


@strawberry.type
class Query:
    event: Event = strawberry.field(resolver=get_event)
    events: List[Event] = strawberry.field(resolver=get_events)


@strawberry.type
class Mutation:
    create_event: Event = strawberry.mutation(resolver=create_event_view)
    update_event: Event = strawberry.mutation(resolver=update_event_view)
    delete_event: str = strawberry.mutation(resolver=delete_event_view)

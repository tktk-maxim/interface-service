import strawberry
from typing import List, Optional
from resolvers.subdivision import (get_subdivision, get_subdivisions, create_subdivision_view,
                                   update_subdivision_view, delete_subdivision_view)
from schemas.subdivision import Subdivision


@strawberry.type
class Query:
    subdivision: Subdivision = strawberry.field(resolver=get_subdivision)
    subdivisions: List[Subdivision] = strawberry.field(resolver=get_subdivisions)


@strawberry.type
class Mutation:
    create_subdivision: Subdivision = strawberry.mutation(resolver=create_subdivision_view)
    update_subdivision: Subdivision = strawberry.mutation(resolver=update_subdivision_view)
    delete_subdivision: str = strawberry.mutation(resolver=delete_subdivision_view)

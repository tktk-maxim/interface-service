import strawberry
from typing import List, AsyncGenerator, Optional
from resolvers.project import (get_project, get_projects, create_project_view,
                               update_project_view, delete_project_view)
from schemas.project import Project
from auth.middleware import IsAuthenticated


@strawberry.type
class Query:
    project: Project = strawberry.field(resolver=get_project, permission_classes=[IsAuthenticated])
    projects: List[Project] = strawberry.field(resolver=get_projects, permission_classes=[IsAuthenticated])


@strawberry.type
class Mutation:
    create_project: Project = strawberry.mutation(resolver=create_project_view, permission_classes=[IsAuthenticated])
    update_project: Project = strawberry.mutation(resolver=update_project_view, permission_classes=[IsAuthenticated])
    delete_project: str = strawberry.mutation(resolver=delete_project_view, permission_classes=[IsAuthenticated])

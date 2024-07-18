import strawberry
from gql.project import Query as ProjectQuery
from gql.project import Mutation as ProjectMutation

from gql.task import Query as TaskQuery
from gql.task import Mutation as TaskMutation


@strawberry.type
class Query(ProjectQuery, TaskQuery):
    pass


@strawberry.type
class Mutation(ProjectMutation, TaskMutation):
    pass


schema = strawberry.Schema(query=Query, mutation=Mutation)

import strawberry
from gql.project import Query as ProjectQuery
from gql.project import Mutation as ProjectMutation

from gql.task import Query as TaskQuery
from gql.task import Mutation as TaskMutation

from gql.employee import Query as EmployeeQuery
from gql.employee import Mutation as EmployeeMutation

from gql.event import Query as EventQuery
from gql.event import Mutation as EventMutation

from gql.subdivision import Query as SubdivisionQuery
from gql.subdivision import Mutation as SubdivisionMutation


@strawberry.type
class Query(ProjectQuery, TaskQuery, SubdivisionQuery, EventQuery, EmployeeQuery):
    pass


@strawberry.type
class Mutation(ProjectMutation, TaskMutation, SubdivisionMutation, EventMutation, EmployeeMutation):
    pass


schema = strawberry.Schema(query=Query, mutation=Mutation)

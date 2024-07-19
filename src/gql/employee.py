import strawberry
from typing import List, Optional
from resolvers.employee import (get_employee, get_employees, create_employee_view,
                                update_employee_view, delete_employee_view)
from schemas.employee import Employee


@strawberry.type
class Query:
    employee: Employee = strawberry.field(resolver=get_employee)
    employees: List[Employee] = strawberry.field(resolver=get_employees)


@strawberry.type
class Mutation:
    create_employee: Employee = strawberry.mutation(resolver=create_employee_view)
    update_employee: Employee = strawberry.mutation(resolver=update_employee_view)
    delete_employee: str = strawberry.mutation(resolver=delete_employee_view)

import strawberry
from typing import List, Optional
from resolvers.employee import (get_employee, get_employees, create_employee_view,
                                update_employee_view, delete_employee_view, search_employee_view)
from schemas.employee import Employee, EmployeeCard
from auth.middleware import IsAuthenticated


@strawberry.type
class Query:
    employee: EmployeeCard = strawberry.field(resolver=get_employee,
                                              permission_classes=[IsAuthenticated])

    employees: List[Employee] = strawberry.field(resolver=get_employees,
                                                 permission_classes=[IsAuthenticated])
    search_employees: List[Employee] = strawberry.field(resolver=search_employee_view,
                                                        permission_classes=[IsAuthenticated])


@strawberry.type
class Mutation:
    create_employee: Employee = strawberry.mutation(resolver=create_employee_view)
    update_employee: Employee = strawberry.mutation(resolver=update_employee_view,
                                                    permission_classes=[IsAuthenticated])
    delete_employee: str = strawberry.mutation(resolver=delete_employee_view,
                                               permission_classes=[IsAuthenticated])

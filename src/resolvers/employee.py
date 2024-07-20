import strawberry
from typing import List, Optional
from crud import get_obj, create_obj, update_obj, delete_obj
from schemas.employee import Employee, EmployeeInput, SearchEmployeeInput, EmployeeCard
from schemas.event import EventForCard
from config import settings


async def get_employee(employee_id: int) -> Optional[EmployeeCard]:
    employee_data = await get_obj(f"http://{settings.user_service_host}:{settings.user_service_port}"
                                  f"/employee/card/{employee_id}")
    employee = EmployeeInput(**employee_data["employee"])
    events = [EventForCard(**event) for event in employee_data["events"]]
    print(employee_data)
    return EmployeeCard(employee=employee, events=events)


async def get_employees() -> List[Employee]:
    employees = await get_obj(f"http://{settings.user_service_host}:{settings.user_service_port}"
                              f"/employee/all/")
    return [Employee(**employee) for employee in employees]


async def create_employee_view(employee: EmployeeInput) -> Optional[Employee]:
    employee_data = await create_obj(f"http://{settings.user_service_host}:{settings.user_service_port}"
                                     f"/employee/create/", data=employee.__dict__)
    return Employee(**employee_data)


async def update_employee_view(employee_id: int, employee: EmployeeInput) -> Optional[Employee]:
    employee_data = await update_obj(f"http://{settings.user_service_host}:{settings.user_service_port}"
                                     f"/employee/{employee_id}", data=employee.__dict__)
    return Employee(**employee_data)


async def delete_employee_view(employee_id: int) -> str:
    employee_data = await delete_obj(f"http://{settings.user_service_host}:{settings.user_service_port}"
                                     f"/employee/{employee_id}")
    return f'Deleted is {employee_data["deleted"]}'


async def search_employee_view(employee: SearchEmployeeInput) -> List[Employee]:
    employees = await get_obj(f"http://{settings.user_service_host}:{settings.user_service_port}"
                              f"/employee/search/?first_name={employee.first_name}"
                              f"&last_name={employee.last_name}"
                              f"&middle_name={employee.middle_name}"
                              f"&login={employee.login}"
                              f"&email={employee.email}")
    return [Employee(**employee) for employee in employees]

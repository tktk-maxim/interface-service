import strawberry
from typing import List, Optional
from crud import get_obj, create_obj, update_obj, delete_obj
from schemas.employee import Employee, EmployeeInput
from config import settings


async def get_employee(employee_id: int) -> Optional[Employee]:
    employee_data = await get_obj(f"http://{settings.user_service_host}:{settings.user_service_port}"
                                  f"/employee/{employee_id}")
    return Employee(**employee_data)


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

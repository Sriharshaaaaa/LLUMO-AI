from fastapi import APIRouter
from models import Employee
from controllers.employee_controller import create_employee

router=APIRouter(prefix="/employees")

@router.post("/",response_model=Employee,status_code=201)
async def create_employee_endpoint(employee:Employee):
    return await create_employee(employee)
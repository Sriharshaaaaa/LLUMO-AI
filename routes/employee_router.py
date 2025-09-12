from fastapi import APIRouter,Path,Body
from models import Employee
from typing import Dict
from controllers.employee_controller import create_employee, delete_employee, get_employee, update_employee

router=APIRouter(prefix="/employees")

@router.post("/",response_model=Employee,status_code=201)
async def create_employee_endpoint(employee:Employee):
    return await create_employee(employee)

@router.get("/{employee_id}",response_model=Employee)
async def get_employee_endpoint(employee_id:str= Path(...,description="Employee's unique ID")):
    return await get_employee(employee_id)

@router.put("/{employee_id}", response_model=Employee)
async def update_employee_endpoint(
    employee_id: str = Path(..., description="Employee's unique ID"),
    updates: Dict = Body(..., example={
        "name": "Updated Name",
        "department": "HR",
        "salary": 65000,
        "joining_date": "2024-01-01",
        "skills": ["interview", "communication"]
    })
):
    # Partial update: we accept any fields to update
    return await update_employee(employee_id, updates)

@router.delete("/{employee_id}")
async def delete_employee_endpoint(employee_id: str = Path(..., description="Employee's unique ID")):
    return await delete_employee(employee_id)
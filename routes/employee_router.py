from fastapi import APIRouter, Depends,Path,Body, Query
from authentication.auth import get_current_user
from models import Employee
from typing import Dict, List
from controllers.employee_controller import create_employee, delete_employee, get_avg_salary_by_department, get_employee, get_employees_by_department, search_employees_by_skill, update_employee

router=APIRouter(prefix="/employees")

# basic end points
@router.post("/",response_model=Employee,status_code=201)
async def create_employee_endpoint(employee:Employee,user :str = Depends(get_current_user)):
    return await create_employee(employee)

# query and aggregate related queries - MUST come before /{employee_id} route
@router.get("/", response_model=List[Employee])
async def list_employees_by_department(
    department: str = Query(..., description="Department name to filter by"),
    limit: int = Query(3,ge=1,le=10,description="No of records to return"),
    skip: int = Query(0,ge=0,description="No of records to skip"),
    user: str = Depends(get_current_user)
    ):
    return await get_employees_by_department(department,limit,skip)

@router.get("/search", response_model=List[Employee])
async def search_employees(
    skill: str = Query(..., description="Skill to search in employees"),
    limit: int = Query(3,ge=1,le=10,description="No of records to return"),
    skip: int = Query(0,ge=0,description="No of records to skip"),
    user: str = Depends(get_current_user)
    ):
    return await search_employees_by_skill(skill,limit,skip)

@router.get("/avg-salary")
async def avg_salary_by_department(user: str = Depends(get_current_user)):
    return await get_avg_salary_by_department()

# Individual employee operations - MUST come after specific routes
@router.get("/{employee_id}",response_model=Employee)
async def get_employee_endpoint(
    employee_id:str= Path(...,description="Employee's unique ID"),
    user:str=Depends(get_current_user)):
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
    }),
    user: str = Depends(get_current_user)
    ):
    # Partial update: we accept any fields to update
    return await update_employee(employee_id, updates)

@router.delete("/{employee_id}")
async def delete_employee_endpoint(employee_id: str = Path(..., description="Employee's unique ID"),user: str = Depends(get_current_user)):
    return await delete_employee(employee_id)
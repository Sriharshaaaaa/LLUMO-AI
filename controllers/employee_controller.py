from fastapi import HTTPException
from models import Employee
from db import employees_collection

async def create_employee(employee:Employee):
    e=await employees_collection.find_one({"employee_id":employee.employee_id})
    if e :
        raise HTTPException(status_code=400,detail="employee already exits")
    doc=employee.model_dump()
    await employees_collection.insert_one(doc)
    return employee
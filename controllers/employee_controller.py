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

async def get_employee(employee_id:str)->Employee:
    employee= await employees_collection.find_one({"employee_id":employee_id})
    if not employee:
        raise HTTPException(status_code=404,detail="Employee not found")
    # MongoDB returns dict with id -remove before returning
    employee.pop("_id",None)
    return Employee(**employee)

async def update_employee(employee_id:str,updates:dict)->Employee:
    # if employee id is being updated
    if "employee_id" in updates and updates["employee_id"]!=employee_id:
        # check if new id already exists
        existing=await employees_collection.find_one({"employee_id":updates["employee_id"]})
        if existing:
            raise HTTPException(status_code=400,detail="New employee already exists")
    
    # performing update
    update_result=await employees_collection.update_one(
        {"employee_id":employee_id},
        {"$set":updates}
    )
    if update_result.matched_count == 0:
        raise HTTPException(status_code=404,detail="Employee not found")
    
    employee= await employees_collection.find_one({"employee_id":employee_id})
    employee.pop("_id",None)
    return Employee(**employee)

async def delete_employee(employee_id:str)->dict:
    delete_res=await employees_collection.delete_one({"employee_id":employee_id})
    if delete_res.deleted_count==0:
        raise HTTPException(status_code=404,detail="Employee not found")
    return {"detail":"Employee deleted successfully"}
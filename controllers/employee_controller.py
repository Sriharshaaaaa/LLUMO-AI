from fastapi import HTTPException
from models import Employee
from db import employees_collection
from typing import List

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

async def get_employees_by_department(department:str)->List[Employee]:
    employees_list=employees_collection.find({"department":department}).sort("joining_date",-1)
    employees=[]
    async for doc in employees_list:
        doc.pop("_id",None)
        employees.append(Employee(**doc))
    return employees

async def search_employees_by_skill(skill: str) -> List[Employee]:
    cursor = employees_collection.find({"skills": skill})
    employees = []
    async for doc in cursor:
        doc.pop("_id", None)
        employees.append(Employee(**doc))
    return employees

async def get_avg_salary_by_department():
    pipeline=[
        {"$group":{
            "_id":"$department",
            "avg_salary":{"$avg","$salary"}
        }},
        {"$project":{
            "department":"$_id",
            "avg_salary":{"$round":["$avg_salary",2]},
            "_id":0   
        }}
    ]
    cursor=employees_collection.aggregate(pipeline)
    results=[]
    async for doc in cursor:
        results.append(doc)
    return results
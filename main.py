from contextlib import asynccontextmanager
from enum import unique
from fastapi import FastAPI
from db import employees_collection
from models import Employee
from controllers.employee_controller import create_employee
from routes.employee_router import router as employee_router

app=FastAPI()

@asynccontextmanager
async def lifespan(app:FastAPI):
    # create indexes
    await employees_collection.create_index("employee_id",unique=True)
    await employees_collection.create_index("department")
    yield

app.include_router(employee_router)
@app.get('/')
async def root():
    return {"message":"Welcome to Employee API"}

# @app.get('/test-db')
# async def test_db():
#     doc=await employees_collection.insert_one({"test":"testing"})
#     return {"inserted_id": str(doc.inserted_id)}

# @app.post("/employees",response_model=Employee,status_code=201)
# async def create_employee_endpoint(employee:Employee):
#     return await create_employee(employee)
from fastapi import FastAPI
from models import Employee
from controllers.employee_controller import create_employee

app=FastAPI()

# @app.get('/')
# async def root():
#     return {"message":"I am Sri Harsha"}

# @app.get('/test-db')
# async def test_db():
#     doc=await employees_collection.insert_one({"test":"testing"})
#     return {"inserted_id": str(doc.inserted_id)}

@app.post("/employees",response_model=Employee,status_code=201)
async def create_employee_endpoint(employee:Employee):
    return await create_employee(employee)
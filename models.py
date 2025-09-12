from pydantic import BaseModel,Field
from typing import List
from datetime import date

class Employee(BaseModel):
    employee_id: str=Field(...,description="Unique identifier for employee")
    name: str=Field(...,description="Employee's full name")
    department: str=Field(...,description="Department name")
    salary: float=Field(...,description="Annual salary")
    joining_date: date=Field(...,description="ISO date when joined")
    skills: List[str]=Field(...,description="List of skills")
        
    class Config:
        schema_extra = {
            "example": {
                "employee_id": "E123",
                "name": "John Doe",
                "department": "Engineering",
                "salary": 75000,
                "joining_date": "2023-01-15",
                "skills": ["Python", "MongoDB", "APIs"]
            }
        }
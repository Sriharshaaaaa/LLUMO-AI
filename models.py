import datetime
from pydantic import BaseModel,Field,validator
from typing import List
from datetime import datetime, date

class Employee(BaseModel):
    employee_id: str=Field(...,description="Unique identifier for employee")
    name: str=Field(...,description="Employee's full name")
    department: str=Field(...,description="Department name")
    salary: float=Field(...,description="Annual salary")
    joining_date: str=Field(...,description="Date in YYYY-MM-DD format")
    skills: List[str]=Field(...,description="List of skills")
    
    @validator('joining_date', pre=True)
    def validate_joining_date(cls, v):
        if isinstance(v, str):
            # Validate the date string format
            try:
                # Try to parse to ensure it's a valid date
                datetime.strptime(v, '%Y-%m-%d')
                return v
            except ValueError:
                # Try ISO format
                try:
                    parsed_date = datetime.fromisoformat(v)
                    return parsed_date.strftime('%Y-%m-%d')
                except ValueError:
                    raise ValueError('Invalid date format. Use YYYY-MM-DD format')
        elif isinstance(v, datetime):
            # If it's already a datetime object, convert to string
            return v.strftime('%Y-%m-%d')
        return v
        
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

class User(BaseModel):
    username:str=Field(...,description="Unique username")
    password:str=Field(...,description="User")
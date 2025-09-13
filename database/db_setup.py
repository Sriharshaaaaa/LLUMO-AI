from motor.motor_asyncio import AsyncIOMotorDatabase

async def create_indexes_and_validation(db:AsyncIOMotorDatabase):
    await db["employees"].create_index("employee_id",unique=True)
    await db["employees"].create_index("deparment")
    
    validator = {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["employee_id", "name", "department", "salary", "joining_date", "skills"],
            "properties": {
                "employee_id": {"bsonType": "string"},
                "name": {"bsonType": "string"},
                "department": {"bsonType": "string"},
                "salary": {"bsonType": ["double", "int"]},
                "joining_date": {
                    "bsonType": "string",
                    "pattern": "^\\d{4}-\\d{2}-\\d{2}$",  # Accepts "YYYY-MM-DD"
                    "description": "Date in ISO format (YYYY-MM-DD)"
                },
                "skills": {
                    "bsonType": "array",
                    "items": {"bsonType": "string"},
                    "description": "List of skills as strings"
                }
            }
        }
    }
    
    try :
        await db.command({
            "collMod":"employees",
            "validator":validator,
            "validationLevel":"moderate"
        })
    except Exception as e:
        print("Schema validation setup failed:",str(e))
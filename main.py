from fastapi import FastAPI
from db import employees_collection

app=FastAPI()

@app.get('/')
async def root():
    return {"message":"I am Sri Harsha"}

@app.get('/test-db')
async def test_db():
    doc=await employees_collection.insert_one({"test":"testing"})
    return {"inserted_id": str(doc.inserted_id)}
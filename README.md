# 🚀 Employee Management API

A FastAPI-based asynchronous REST API for managing employee data, featuring integration with MongoDB, user authentication, and advanced query/filter functionality.

---

## 🛠️ Tech Stack

- **Backend:** FastAPI (async)
- **Database:** MongoDB (via Motor - async driver)
- **Authentication:** JWT-based login
- **Other Tools:** Pydantic, Uvicorn, Passlib, Bcrypt

---

## 📁 Project Structure
├── controllers/ # Business logic for employees
├── models/ # Pydantic models (request/response)
├── routes/ # API route handlers
├── auth/ # Authentication logic (JWT, hashing)
├── database/ # MongoDB connection setup
├── main.py # FastAPI app entry point
├── README.md # This file
└── requirements.txt # Dependencies

## 📦 Features

- ✅ Add, update, delete employee records
- ✅ Search by department, skill
- ✅ Paginated queries with filters
- ✅ JWT-based user login and protected routes
- ✅ MongoDB aggregation for average salary by department
- ✅ Robust input validation with Pydantic

## 🚀 Getting Started

###
1. Clone the Repository
in your terminal

git clone https://github.com/your-username/employee-api.git
cd employee-api 

2. Create Virtual Environment
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows

3. Install Dependencies
pip install -r requirements.txt

4. Start MongoDB
Ensure MongoDB is running locally

5. Run the App
uvicorn main:app --reload

App will be available at: http://127.0.0.1:8000/


🔐 Authentication
Endpoint
POST /login

Sample Request
{
  "username": "admin",
  "password": "admin123"
}

Returns a JWT access token. Use it in Authorization header for protected endpoints:
Authorization: Bearer <token>


📚 Example Endpoints
Method	Endpoint	Description
GET	/employees/	List employees by department
GET	/employees/search?skill=ML	Search by skill
GET	/employees/avg-salary	Avg salary by department
POST	/employees/	Add new employee
PUT	/employees/{employee_id}	Update employee by ID
DELETE	/employees/{employee_id}	Delete employee by ID

🧪 Testing
Use Postman or FastAPI Swagger UI at:
http://127.0.0.1:8000/docs



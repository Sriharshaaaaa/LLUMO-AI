# 🚀 Employee Management API

A FastAPI-based asynchronous REST API for managing employee data, featuring MongoDB integration, user authentication, and powerful query/filter capabilities.

---

## 🛠️ Tech Stack

- **Backend:** FastAPI (async)  
- **Database:** MongoDB (with Motor async driver)  
- **Authentication:** JWT-based login with password hashing (bcrypt)  
- **Validation:** Pydantic models for request and response data  
- **Server:** Uvicorn for ASGI deployment  

---

## 📁 Project Structure
- ├── controllers/ # Business logic for employees
- ├── models.py # Pydantic models (Employee, User)
- ├── routers/ # API route handlers (employees, auth)
- ├── auth.py # Authentication utilities (JWT, hashing)
- ├── database/ # MongoDB connection and setup (indexes, schema validation)
- ├── main.py # FastAPI app entry point
- ├── README.md # Project documentation (this file)
- └── requirements.txt # Dependencies


---

## 📦 Features

- ✅ CRUD: Add, update, delete employee records  
- ✅ Search employees by department and skill with pagination support  
- ✅ MongoDB aggregation for average salary by department  
- ✅ JWT authentication with secure password hashing  
- ✅ Protected API endpoints requiring authorization via JWT token  
- ✅ Robust input validation via Pydantic  
- ✅ MongoDB indexes on `employee_id` (unique) and `department` for query performance  
- ✅ API documentation accessible via Swagger UI

---

## 🚀 Getting Started

### 1. Clone the Repository
git clone https://github.com/your-username/employee-api.git
cd employee-api

### 2. Create and Activate Virtual Environment
python -m venv .venv
Windows:
.venv\Scripts\activate


### 3. Install Dependencies
pip install -r requirements.txt


### 4. Start MongoDB
Make sure MongoDB is running locally on default port.

### 5. Run the Application
uvicorn main:app --reload
Access the API at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🔐 Authentication Workflow

- **Register:** New users must register first to create an account by providing a unique username and password.  
- **Login:** After registering, users login to get a JWT access token by posting credentials to `/login`.  
- **Use Token:** Include the JWT token in all protected requests’ `Authorization` header as:  
  `Authorization: Bearer <token>`
- Without a valid token, protected endpoints (employees CRUD and queries) cannot be accessed.

---

## 📚 API Endpoints Overview

| Method | Endpoint                      | Description                          | Notes                              |
|--------|-------------------------------|------------------------------------|-----------------------------------|
| POST   | `/register`                   | Register new user                   | Username must be unique            |
| POST   | `/login`                     | Authenticate user and get JWT token| Returns access token               |
| GET    | `/employees/`                | List employees by department       | Supports pagination (limit, skip) |
| GET    | `/employees/search`          | Search employees by skill           | Pagination supported              |
| GET    | `/employees/avg-salary`      | Average salary per department       | MongoDB aggregation               |
| POST   | `/employees/`                | Add new employee                    | Protected, requires JWT           |
| PUT    | `/employees/{employee_id}`   | Update employee details             | Partial updates allowed           |
| DELETE | `/employees/{employee_id}`   | Delete employee                    | Protected, requires JWT           |

---

## 🧩 Pagination & Indexing

- **Pagination:**  
  List and search endpoints support `limit` and `skip` query parameters to manage result size and offset, improving performance and usability.

- **Indexes:**  
  MongoDB creates indexes on `employee_id` (unique) to enforce uniqueness and speed up lookups, and on `department` to accelerate filtering operations.

---

## 🧪 Testing & Documentation

- Use FastAPI’s interactive Swagger UI to explore and test the API:  
  [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Or use tools like Postman or curl for manual endpoint testing.

---


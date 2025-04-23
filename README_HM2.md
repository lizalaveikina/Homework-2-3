# Basic REST-based application with Token authentication

This project demonstrates a simple microservice architecture using **FastAPI**. 
It consists of three independent microservices communicating via HTTP, with one public-facing service protected by token-based authentication.

---

## Purpose of the Assignment

The goal of this assignment was to:
- Understand the basics of microservice architecture.
- Learn how to build and run multiple FastAPI applications.
- Implement communication and orchestration between services.
- Add basic token-based authentication to secure a public endpoint.

---

## Microservices Overview

### 1. **Database Service** (`db_service.py`)
- In-memory storage (Python list).
- Endpoints:
  - `POST /save`: saves incoming JSON data.
  - `GET /get`: retrieves all stored data.
  - `GET /health`: health check.
  - `GET /`: short description.

### 2. **Business Logic Service** (`business_service.py`)
- Simulates a time-consuming data processing operation.
- Endpoints:
  - `POST /process`: processes input data (with `time.sleep(2)` delay).
  - `GET /health`: health check.
  - `GET /`: short description.

### 3. **Client Service** (`client_service.py`)
- The only publicly accessible service.
- Orchestrates data flow between the other two services.
- Protected by token-based authentication.
- Endpoints:
  - `POST /run`: main orchestration endpoint (requires token).
  - `GET /health`: health check.
  - `GET /`: short description.

---

## Token-Based Authentication

The `/run` endpoint of the **Client Service** is protected by a hardcoded token.

### Token:
```python
APP_TOKEN = "Secret123"
```

### Required HTTP Header:
```
Authorization: Bearer Secret123
```

If the token is missing or incorrect, the client receives:
```json
{
  "detail": "Unauthorized"
}
```

---

## Request Flow

```text
Client
  ↓
Client Service (/run)
  → calls Database Service (/get)
  → calls Business Logic Service (/process)
  → calls Database Service (/save)
  ↓
Returns processed result to client
```

---

## Example Usage (cURL)

### 1️⃣ Save Data to the Database Service
```bash
curl -X POST http://localhost:8002/save \
     -H "Content-Type: application/json" \
     -d '{"text": "Hello, world!"}'
```

### 2️⃣ Trigger the Full Flow via Client Service
```bash
curl -X POST http://localhost:8000/run \
     -H "Authorization: Bearer Secret123"
```

### Expected Output:
```json
{
  "result": {
    "original": {
      "text": "Hello, world!"
    },
    "processed": true
  }
}
```

---

## Health Check Endpoints

Each microservice has two utility endpoints:

- `GET /` → returns a short description of the service
- `GET /health` → returns:
```json
{ "status": "ok" }
```

You can test them using:
```bash
curl http://localhost:8000/health
curl http://localhost:8001/health
curl http://localhost:8002/health
```

---

## How to Run the Services

Ensure that Python 3 is installed.

### 1. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Each Service in Separate Terminal Tabs or Windows

#### Terminal 1 — Database Service (port 8002):
```bash
uvicorn db_service:app --port 8002
```

#### Terminal 2 — Business Logic Service (port 8001):
```bash
uvicorn business_service:app --port 8001
```

#### Terminal 3 — Client Service (port 8000):
```bash
uvicorn client_service:app --port 8000
```

---

## Requirements

This project uses the following Python packages:
- fastapi
- uvicorn
- requests

Install them via:
```bash
pip install -r requirements.txt
```

---

## Author

Created by **Yelyzaveta Laveikina**  
Course: *Architecture of IT Solutions*  
University: Ukrainian Catholic University (UCU)




# Containerization with Podman

This project builds upon Homework #2 and demonstrates how to containerize and orchestrate a FastAPI-based microservice architecture using **Podman** and **Podman Compose**.

The system includes authentication, inter-service communication, and fully automated local container deployment.

---

## Microservices Architecture

This system consists of three FastAPI services:

### 1. `client_service.py` – Port **8000**
- Public-facing endpoint
- Protected via Bearer Token
- Orchestrates business and database services

### 2. `business_service.py` – Port **8001**
- Simulates time-consuming data processing

### 3. `db_service.py` – Port **8002**
- In-memory database with JSON API

---

## Authentication

The `/run` endpoint in `client_service` requires a token.

```http
Authorization: Bearer Secret123
```

---

## Container Setup

Each service has its own Dockerfile:

- Dockerfile.client
- Dockerfile.business
- Dockerfile.db

All services are described in podman-compose.yml and run in the same virtual network (backend).

---

## Prerequisites

Make sure you have the following installed:

- Podman
- Podman Compose

To install on macOS:

```bash 
brew install podman podman-compose
podman machine init
podman machine start
```

---

## Run the Project

Build and start all services

```bash 
podman-compose up --build
```

You will see logs for each container (client, business, db).

---

## Testing the System

1. Check Health Status

```bash
curl http://localhost:8000/health
curl http://localhost:8001/health
curl http://localhost:8002/health
```

All should return:

```json
{ "status": "ok" }
```

2. Save Data to DB

```bash
curl -X POST http://localhost:8002/save \
     -H "Content-Type: application/json" \
     -d '{"text": "Hello, world!"}'
```

3. Trigger Orchestration via Client
```bash
curl -X POST http://localhost:8000/run \
     -H "Authorization: Bearer Secret123"
```

Expected response:

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

## Clean Up

To stop and remove all services:

```bash
podman-compose down
```

---

## Author

Created by **Yelyzaveta Laveikina**  
Course: *Architecture of IT Solutions*  
University: Ukrainian Catholic University (UCU)

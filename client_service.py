from fastapi import FastAPI, Header, HTTPException
import requests

APP_TOKEN = "Secret123"

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Client Service: connects all services"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/run")
def run(authorization: str = Header(None)):
    
    if authorization != f"Bearer {APP_TOKEN}":
        raise HTTPException(status_code=401, detail="Unauthorized")

    db_response = requests.get("http://localhost:8002/get")
    data = db_response.json().get("data", [])

    if not data:
        return {"error": "No data in DB"}

    to_process = data[-1]

    process_response = requests.post("http://localhost:8001/process", json=to_process)
    processed = process_response.json()

    requests.post("http://localhost:8002/save", json=processed)

    return {"result": processed}

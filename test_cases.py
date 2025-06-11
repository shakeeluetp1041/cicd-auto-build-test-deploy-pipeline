# The file name must start with test, needed for pytest
from fastapi.testclient import TestClient # this client communicate with faastapi app without the need for uvicorn sever ruuning
from app_fastapi import app


client = TestClient(app) # instance of a client

def test_root_get():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_fibonacci_valid():
    response = client.post("/fibonacci", json={"count": 5})
    assert response.status_code == 200
    assert response.json() == {"fibonacci": [0, 1, 1, 2, 3]}

def test_fibonacci_zero():
    response = client.post("/fibonacci", json={"count": 0})
    assert response.status_code == 200
    assert response.json() == {"fibonacci": []}

def test_fibonacci_negative():
    response = client.post("/fibonacci", json={"count": -1})
    assert response.status_code == 200
    assert response.json() == {"error": "Count must be non-negative"}

def test_fibonacci_invalid_payload():
    response = client.post("/fibonacci", json={"value": 3})
    assert response.status_code == 422  # Unprocessable Entity due to missing 'count'

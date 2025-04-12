from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_volunteer():
    response = client.post("/volunteers/", json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"
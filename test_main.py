import json
from dotenv import load_dotenv
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)
load_dotenv()


def register():
    data = {
        "username": "kyliazzz",
        "email": "kylian@hotmail.com",
        "password": "1234567"
    }
    response = client.post(
        "/register", headers={"X-Token": "coneofsilence"}, data=json.dumps(data))
    assert response.status_code == 200

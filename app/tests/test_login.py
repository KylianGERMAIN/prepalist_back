import json
from fastapi.testclient import TestClient
from app.utils.custom_error_message import Custom_Error_Message
from main import app

client = TestClient(app)


def test_login_success():
    data = {
        "username": "kyliazzz",
        "email": "kylian1@hotmail.com",
        "password": "1234567"
    }
    response = client.post(
        "/login", headers={"X-Token": "coneofsilence"}, data=json.dumps(data))
    assert response.status_code == 200


def test_login_with_bad_password():
    data = {
        "username": "kyliazzz",
        "email": "kylian1@hotmail.com",
        "password": "1234567"
    }
    response = client.post(
        "/login", headers={"X-Token": "coneofsilence"}, data=json.dumps(data))
    assert response.status_code == 403
    response = response.json()
    print(response)
    assert response['detail'] == Custom_Error_Message.NO_AUTHORIZATION.value

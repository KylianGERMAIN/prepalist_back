from unittest import TestCase
import json
from fastapi.testclient import TestClient
import httpx
from app.utils.custom_error_message import Custom_Error_Message


def test_login_success():
    data = {
        "username": "kyliazzz",
        "email": "kylian10@hotmail.com",
        "password": "1234567"
    }
    response = httpx.post(
        "http://127.0.0.1:8000/api/v1/login/", headers={"X-Token": "coneofsilence"}, data=json.dumps(data))
    assert response.status_code == 200


def test_login_with_bad_password():
    data = {
        "username": "kyliazzz",
        "email": "kylian10@hotmail.com",
        "password": "12345674"
    }
    response = httpx.post(
        "http://127.0.0.1:8000/api/v1/login/", headers={"X-Token": "coneofsilence"}, data=json.dumps(data))
    assert response.status_code == 403
    response = response.json()
    assert response['detail'] == Custom_Error_Message.BAD_PASSWORD.value

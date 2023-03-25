import json
from fastapi.testclient import TestClient
from app.utils.custom_error_message import Custom_Error_Message
from main import app

client = TestClient(app)


def test_register_success():
    data = {
        "username": "kyliazzz",
        "email": "kylian1@hotmail.com",
        "password": "1234567"
    }
    response = client.post(
        "/register", headers={"X-Token": "coneofsilence"}, data=json.dumps(data))
    assert response.status_code == 200


def test_register_with_short_username():
    data = {
        "username": "ky",
        "email": "kylian@hotmail.com",
        "password": "1234567"
    }
    response = client.post(
        "/register", headers={"X-Token": "coneofsilence"}, data=json.dumps(data))
    assert response.status_code == 403
    response = response.json()
    assert response['detail'] == Custom_Error_Message.USERNAME_LENGTH.value


def test_register_with_bad_email():
    data = {
        "username": "kylian",
        "email": "kylian",
        "password": "1234567"
    }
    response = client.post(
        "/register", headers={"X-Token": "coneofsilence"}, data=json.dumps(data))
    assert response.status_code == 403
    response = response.json()
    assert response['detail'] == Custom_Error_Message.INVALID_EMAIL_ADRESS.value


def test_register_with_short_password():
    data = {
        "username": "kylian",
        "email": "kylian@hotmail.com",
        "password": "12"
    }
    response = client.post(
        "/register", headers={"X-Token": "coneofsilence"}, data=json.dumps(data))
    assert response.status_code == 403
    response = response.json()
    assert response['detail'] == Custom_Error_Message.PASSWORD_LENGTH.value

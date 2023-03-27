import json
import os
import httpx
from app.utils.custom_error_message import Custom_Error_Message


def test_meal_success():
    data = {
        "name": "pate carbonara",
        "ingredients": [
            {
                "ingredient": "pate"
            },
            {
                "ingredient": "creme fraiche"
            },
            {
                "ingredient": "lardon"
            }
        ]
    }
    response = httpx.post(
        "http://127.0.0.1:8000/meal/", headers={"Authorization": os.getenv(
            'JWT_SECRET_TEST_LOGIN_TOKEN')}, data=json.dumps(data))
    assert response.status_code == 200


def test_meal_with_bad_token():
    data = {
        "name": "sandwitch Jambon beurre",
        "ingredients": [
            {
                "ingredient": "pain"
            },
            {
                "ingredient": "jambon"
            },
            {
                "ingredient": "beurre"
            }
        ]
    }
    response = httpx.post(
        "http://127.0.0.1:8000/meal/", headers={"Authorization": "hello world"}, data=json.dumps(data))
    assert response.status_code == 403
    response = response.json()
    assert response['detail'] == Custom_Error_Message.INVALID_TOKEN.value


def test_meal_with_no_token():
    data = {
        "name": "sandwitch Jambon beurre",
        "ingredients": [
            {
                "ingredient": "pain"
            },
            {
                "ingredient": "jambon"
            },
            {
                "ingredient": "beurre"
            }
        ]
    }
    response = httpx.post(
        "http://127.0.0.1:8000/meal/", headers={}, data=json.dumps(data))
    assert response.status_code == 401
    response = response.json()
    assert response['detail'] == Custom_Error_Message.NO_AUTHORIZATION.value


def test_meal_with_no_ingrediants():
    data = {
        "name": "sandwitch Jambon beurre",
        "ingredients": []
    }
    response = httpx.post(
        "http://127.0.0.1:8000/meal/", headers={"Authorization": os.getenv(
            'JWT_SECRET_TEST_LOGIN_TOKEN')}, data=json.dumps(data))
    assert response.status_code == 403
    response = response.json()
    assert response['detail'] == Custom_Error_Message.NO_INGREDIENTS.value


def test_meal_already_exist():
    data = {
        "name": "pate carbonara",
        "ingredients": [
            {
                "ingredient": "pate"
            },
            {
                "ingredient": "creme fraiche"
            },
            {
                "ingredient": "lardon"
            }
        ]
    }
    response = httpx.post(
        "http://127.0.0.1:8000/meal/", headers={"Authorization": os.getenv(
            'JWT_SECRET_TEST_LOGIN_TOKEN')}, data=json.dumps(data))
    assert response.status_code == 409
    response = response.json()
    assert response['detail'] == Custom_Error_Message.MEAL_ALREADY_EXIST.value
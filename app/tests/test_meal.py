import json
import os
import httpx
from app.utils.custom_error_message import Custom_Error_Message


def delete_meal_(id: str):
    response = httpx.delete(
        "http://127.0.0.1:8000/api/v1/meal/"+id, headers={"Authorization": os.getenv(
            'JWT_SECRET_TEST_LOGIN_TOKEN')})
    assert response.status_code == 202


def test_update_meal():
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
    data_update = {
        "name": "pate bolognaise",
        "ingredients": [
            {
                "ingredient": "pate"
            },
            {
                "ingredient": "sauce tomate"
            },
            {
                "ingredient": "boulette de viande"
            }
        ]
    }
    response = httpx.post(
        "http://127.0.0.1:8000/api/v1/meal/", headers={"Authorization": os.getenv(
            'JWT_SECRET_TEST_LOGIN_TOKEN')}, data=json.dumps(data))
    assert response.status_code == 201
    response = response.json()
    response = httpx.put(
        "http://127.0.0.1:8000/api/v1/meal/" + response['id'], headers={"Authorization": os.getenv(
            'JWT_SECRET_TEST_LOGIN_TOKEN')}, data=json.dumps(data_update))
    assert response.status_code == 200
    response = response.json()
    assert response['name'] == "pate bolognaise"
    delete_meal_(response['id'])


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
        "http://127.0.0.1:8000/api/v1/meal/", headers={"Authorization": os.getenv(
            'JWT_SECRET_TEST_LOGIN_TOKEN')}, data=json.dumps(data))
    assert response.status_code == 201
    response = response.json()
    delete_meal_(response['id'])


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
        "http://127.0.0.1:8000/api/v1/meal/", headers={"Authorization": "hello world"}, data=json.dumps(data))
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
        "http://127.0.0.1:8000/api/v1/meal/", headers={}, data=json.dumps(data))
    assert response.status_code == 401
    response = response.json()
    assert response['detail'] == Custom_Error_Message.NO_AUTHORIZATION.value


def test_meal_with_no_ingrediants():
    data = {
        "name": "sandwitch Jambon beurre",
        "ingredients": []
    }
    response = httpx.post(
        "http://127.0.0.1:8000/api/v1/meal/", headers={"Authorization": os.getenv(
            'JWT_SECRET_TEST_LOGIN_TOKEN')}, data=json.dumps(data))
    assert response.status_code == 403
    response = response.json()
    assert response['detail'] == Custom_Error_Message.NO_INGREDIENTS.value


def test_meal_already_exist():
    data = {
        "name": "test",
        "ingredients": [
            {
                "ingredient": "test"
            }
        ]
    }
    response = httpx.post(
        "http://127.0.0.1:8000/api/v1/meal/", headers={"Authorization": os.getenv(
            'JWT_SECRET_TEST_LOGIN_TOKEN')}, data=json.dumps(data))
    assert response.status_code == 409
    response = response.json()
    assert response['detail'] == Custom_Error_Message.MEAL_ALREADY_EXIST.value

import json
import os
import httpx
from app.utils.custom_error_message import Custom_Error_Message


def delete_meal_(id: str):
    response = httpx.delete(
        "http://127.0.0.1:8000/api/v2/meal/"+id, headers={"Authorization": os.getenv(
            'JWT_SECRET_TEST_LOGIN_TOKEN')})
    assert response.status_code == 202


def test_update_meal():
    data = {
        "name": "pate carbonara",
        "ingredients": [
                {
                    "ingredient": "pate",
                    "quantity": 100,
                    "unit": "g"
                },
            {
                    "ingredient": "creme fraiche",
                    "quantity": 12.5,
                    "unit": "cL"
                },
            {
                    "ingredient": "lardon",
                    "quantity": 62.5,
                    "unit": "g"
                }
        ]
    }
    data_update = {
        "name": "pate bolognaise",
        "ingredients": [
            {
                "ingredient": "pate",
                "quantity": 125,
                "unit": "g"
            },
            {
                "ingredient": "sauce tomate",
                "quantity": 125,
                "unit": "g"
            },
            {
                "ingredient": "boulette de viande",
                "quantity": 75,
                "unit": "g"
            }
        ]
    }
    response = httpx.post(
        "http://127.0.0.1:8000/api/v2/meal/", headers={"Authorization": os.getenv(
            'JWT_SECRET_TEST_LOGIN_TOKEN')}, data=json.dumps(data))
    assert response.status_code == 201
    response = response.json()
    response = httpx.put(
        "http://127.0.0.1:8000/api/v2/meal/" + response['id'], headers={"Authorization": os.getenv(
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
                "ingredient": "pate",
                "quantity": 100,
                "unit": "g"
            },
            {
                "ingredient": "creme fraiche",
                "quantity": 12.5,
                "unit": "cL"
            },
            {
                "ingredient": "lardon",
                "quantity": 62.5,
                "unit": "g"
            }
        ]
    }
    response = httpx.post(
        "http://127.0.0.1:8000/api/v2/meal/", headers={"Authorization": os.getenv(
            'JWT_SECRET_TEST_LOGIN_TOKEN')}, data=json.dumps(data))
    assert response.status_code == 201
    response = response.json()
    delete_meal_(response['id'])


def test_meal_with_bad_token():
    data = {
        "name": "sandwitch Jambon beurre",
        "ingredients": [
            {
                "ingredient": "pain",
                "quantity": 1,
                "unit": "unit"
            },
            {
                "ingredient": "jambon",
                "quantity": 1,
                "unit": "unit"
            },
            {
                "ingredient": "beurre",
                "quantity": 10,
                "unit": "g"
            }
        ]
    }
    response = httpx.post(
        "http://127.0.0.1:8000/api/v2/meal/", headers={"Authorization": "hello world"}, data=json.dumps(data))
    assert response.status_code == 403
    response = response.json()
    assert response['detail'] == Custom_Error_Message.INVALID_TOKEN.value


def test_meal_with_no_token():
    data = {
        "name": "sandwitch Jambon beurre",
        "ingredients": [
            {
                "ingredient": "pain",
                "quantity": 1,
                "unit": "unit"
            },
            {
                "ingredient": "jambon",
                "quantity": 1,
                "unit": "unit"
            },
            {
                "ingredient": "beurre",
                "quantity": 10,
                "unit": "g"
            }
        ]
    }
    response = httpx.post(
        "http://127.0.0.1:8000/api/v2/meal/", headers={}, data=json.dumps(data))
    assert response.status_code == 403
    response = response.json()
    assert response['detail'] == Custom_Error_Message.INVALID_TOKEN.value


def test_meal_with_no_ingrediants():
    data = {
        "name": "sandwitch Jambon beurre",
        "ingredients": []
    }
    response = httpx.post(
        "http://127.0.0.1:8000/api/v2/meal/", headers={"Authorization": os.getenv(
            'JWT_SECRET_TEST_LOGIN_TOKEN')}, data=json.dumps(data))
    assert response.status_code == 403
    response = response.json()
    assert response['detail'] == Custom_Error_Message.NO_INGREDIENTS.value


def test_meal_already_exist():
    data = {
        "name": "test",
        "ingredients": [
            {
                "ingredient": "test",
                "quantity": 10,
                "unit": "g"
            }
        ]
    }
    response = httpx.post(
        "http://127.0.0.1:8000/api/v2/meal/", headers={"Authorization": os.getenv(
            'JWT_SECRET_TEST_LOGIN_TOKEN')}, data=json.dumps(data))
    assert response.status_code == 409
    response = response.json()
    assert response['detail'] == Custom_Error_Message.MEAL_ALREADY_EXIST.value

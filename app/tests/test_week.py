import os
import json
import httpx


def test_create_my_week():
    data = {
        "week": [
            {
                "date": "2023-05-22 00:00:00",
                "lunch": {
                    "name": "",
                    "id": "",
                        "serving": 1
                },
                "dinner": {
                    "name": "Ratatouille",
                    "id": "64259df6167322f7ecf61cc8",
                    "serving": 1
                }
            },
            {
                "date": "2023-05-23 00:00:00",
                "lunch": {
                    "name": "Ratatouille",
                    "id": "64259df6167322f7ecf61cc8",
                    "serving": 1
                },
                "dinner": {
                    "name": "Boulettes de boeuf aux petits pois-carottes",
                    "id": "6425997a167322f7ecf61cbf",
                    "serving": 1
                }
            },
            {
                "date": "2023-05-24 00:00:00",
                "lunch": {
                    "name": "Boulettes de boeuf aux petits pois-carottes",
                    "id": "6425997a167322f7ecf61cbf",
                    "serving": 1
                },
                "dinner": {
                    "name": "Lasagnes",
                    "id": "64259b77167322f7ecf61cc5",
                    "serving": 1
                }
            },
            {
                "date": "2023-05-25 00:00:00",
                "lunch": {
                    "name": "Lasagnes",
                    "id": "64259b77167322f7ecf61cc5",
                    "serving": 1
                },
                "dinner": {
                    "name": "Nuggets et frites",
                    "id": "642598bf167322f7ecf61cbd",
                    "serving": 1
                }
            },
            {
                "date": "2023-05-26 00:00:00",
                "lunch": {
                    "name": "Nuggets et frites",
                    "id": "642598bf167322f7ecf61cbd",
                    "serving": 1
                },
                "dinner": {
                    "name": "Pizza",
                    "id": "642598d9167322f7ecf61cbe",
                    "serving": 1
                }
            },
            {
                "date": "2023-05-27 00:00:00",
                "lunch": {
                    "name": "Pizza",
                    "id": "642598d9167322f7ecf61cbe",
                    "serving": 1
                },
                "dinner": {
                    "name": "Pommes de terre aux petits lardons",
                    "id": "64259b2b167322f7ecf61cc4",
                    "serving": 1
                }
            },
            {
                "date": "2023-05-28 00:00:00",
                "lunch": {
                    "name": "Pommes de terre aux petits lardons",
                    "id": "64259b2b167322f7ecf61cc4",
                    "serving": 1
                },
                "dinner": {
                    "name": "Wraps",
                    "id": "64259888167322f7ecf61cbc",
                    "serving": 1
                }
            }
        ]


    }
    response = httpx.post(
        "http://127.0.0.1:8000/api/v1/week/", headers={"Authorization": os.getenv(
            'JWT_SECRET_TEST_LOGIN_TOKEN')}, data=json.dumps(data))

    assert response.status_code == 200


def test_create_my_week_no_enought_day():
    data = {
        "week": [
        ]
    }
    response = httpx.post(
        "http://127.0.0.1:8000/api/v1/week/", headers={"Authorization": os.getenv(
            'JWT_SECRET_TEST_LOGIN_TOKEN')}, data=json.dumps(data))

    assert response.status_code == 403


def test_get_my_week():
    response = httpx.get(
        "http://127.0.0.1:8000/api/v1/week/", headers={"Authorization": os.getenv(
            'JWT_SECRET_TEST_LOGIN_TOKEN')})

    assert response.status_code == 200

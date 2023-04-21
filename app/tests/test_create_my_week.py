import os
import json
import httpx
from app.utils.custom_error_message import Custom_Error_Message


def test_create_my_week():
    response = httpx.get(
        "http://127.0.0.1:8000/create_my_week/", headers={"Authorization": os.getenv(
            'JWT_SECRET_TEST_LOGIN_TOKEN')})

    assert response.status_code == 200

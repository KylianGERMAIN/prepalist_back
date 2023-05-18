import os
from unittest import TestCase
import json
from fastapi.testclient import TestClient
import httpx
from app.utils.custom_error_message import Custom_Error_Message


def test_refresh_token_success():
    response = httpx.get(
        "http://127.0.0.1:8000/api/v1/refresh_token/", headers={"Authorization": os.getenv(
            'JWT_SECRET_TEST_LOGIN_REFRESH_TOKEN')})
    assert response.status_code == 200

import os
from unittest import TestCase
import json
from fastapi.testclient import TestClient
import httpx
from app.utils.custom_error_message import Custom_Error_Message


def test_test_success():
    response = httpx.get(
        "http://127.0.0.1:8000/api/v1/list/", headers={"Authorization": os.getenv(
            'JWT_SECRET_TEST_LOGIN_TOKEN')})
    assert response.status_code == 200

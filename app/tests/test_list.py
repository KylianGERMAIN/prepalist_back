import os
import httpx


def test_test_success():
    response = httpx.get(
        "http://127.0.0.1:8000/api/v1/list/", headers={"Authorization": os.getenv(
            'JWT_SECRET_TEST_LOGIN_TOKEN')})
    assert response.status_code == 200

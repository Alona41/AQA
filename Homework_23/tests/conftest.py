# tests/conftest.py
import pytest
import requests
from requests.auth import HTTPBasicAuth


@pytest.fixture(scope="class")
def auth_session():
    session = requests.Session()
    auth_url = "http://127.0.0.1:8080/auth"
    username = "test_user"
    password = "test_pass"

    # Виконуємо аутентифікацію
    response = session.post(auth_url, auth=HTTPBasicAuth(username, password))
    assert response.status_code == 200, "Помилка аутентифікації"

    access_token = response.json().get("access_token")
    session.headers.update({'Authorization': 'Bearer ' + access_token})
    return session

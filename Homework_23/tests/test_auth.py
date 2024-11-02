# tests/test_auth.py
import requests
from requests.auth import HTTPBasicAuth


def test_auth():
    auth_url = "http://127.0.0.1:8080/auth"
    response = requests.post(auth_url, auth=HTTPBasicAuth("test_user", "test_pass"))

    assert response.status_code == 200, "Помилка аутентифікації"
    assert "access_token" in response.json(), "Відсутній токен доступу у відповіді"

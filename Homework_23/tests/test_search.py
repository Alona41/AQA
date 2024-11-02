# tests/test_search.py
import pytest
import logging

# Налаштування логування у файл та консоль
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("logs/test_search.log"),
                        logging.StreamHandler()
                    ])
logger = logging.getLogger(__name__)


@pytest.mark.parametrize("sort_by, limit", [
    ("price", 5),
    ("year", 3),
    ("engine_volume", 2),
    ("brand", 4),
    ("price", 1),
    (None, None),  # Без параметрів
])
def test_search_cars(auth_session, sort_by, limit):
    search_url = "http://127.0.0.1:8080/cars"
    params = {}
    if sort_by:
        params["sort_by"] = sort_by
    if limit:
        params["limit"] = limit

    # Виконуємо GET-запит для пошуку автомобілів
    response = auth_session.get(search_url, params=params)
    assert response.status_code == 200, f"Очікуваний статус 200, але отримано {response.status_code}"

    cars = response.json()
    assert isinstance(cars, list), "Відповідь повинна бути списком автомобілів"

    # Логування результатів тесту
    logger.info(f"Тест із параметрами sort_by={sort_by}, limit={limit} - Успішно. "
                f"Отримано {len(cars)} записів.")

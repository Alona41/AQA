import json
import logging


def validate_json(file_path):
    """
    Перевіряє валідність JSON-файлу. Якщо файл невалідний, записує помилку у лог.

    :param file_path: шлях до JSON-файлу
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            json.load(f)  # Якщо файл невалідний, згенерується помилка
    except json.JSONDecodeError as e:
        logging.error(f'Invalid JSON in file: {file_path} - {e}')

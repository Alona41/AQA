import logging
from datetime import datetime

def analyze_log(file_path):
    # Налаштування логування для запису в файл hb_test.log з кодуванням UTF-8
    logging.basicConfig(
        filename='hb_test.log',
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s',
        encoding='utf-8'  # Встановлюємо кодування UTF-8
    )

    # Тестовий запис для перевірки логування
    logging.info("Початок аналізу лог-файлу...")

    filtered_log = []
    key = "Key TSTFEED0300|7E3E|0400"

    # Читання лог-файлу
    with open(file_path, 'r', encoding='utf-8') as file:  # Додаємо кодування UTF-8 для читання
        lines = file.readlines()

        # Відбір рядків з потрібним ключем
        for line in lines:
            if key in line:
                filtered_log.append(line.strip())

    # Перебір відфільтрованих рядків для аналізу часу
    for i in range(len(filtered_log) - 1):
        # Отримуємо час з поточного і наступного рядка
        current_time_str = filtered_log[i].find("Timestamp ") + len("Timestamp ")
        next_time_str = filtered_log[i + 1].find("Timestamp ") + len("Timestamp ")

        # Перетворюємо строку в час
        current_time = datetime.strptime(filtered_log[i][current_time_str:current_time_str + 8], "%H:%M:%S")
        next_time = datetime.strptime(filtered_log[i + 1][next_time_str:next_time_str + 8], "%H:%M:%S")

        # Обчислюємо різницю у секундах
        heartbeat = (next_time - current_time).total_seconds()

        # Логування в залежності від значення heartbeat
        if 31 < heartbeat < 33:
            logging.warning(f"Heartbeat warning: {heartbeat} seconds at {current_time.strftime('%H:%M:%S')}")
        elif heartbeat >= 33:
            logging.error(f"Heartbeat error: {heartbeat} seconds at {current_time.strftime('%H:%M:%S')}")

    # Повідомлення про завершення аналізу
    logging.info("Аналіз лог-файлу завершено.")

# Виклик функції з шляхом до лог-файлу
analyze_log('C:/Users/cluba/PycharmProjects/AQA/homework_21/hblog.txt')

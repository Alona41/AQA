from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Ініціалізація ChromeDriver через Service та WebDriver Manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Відкриваємо головну сторінку
driver.get("http://localhost:8000/dz.html")

# Секретний текст для кожного фрейму
frame1_secret = "Frame1_Secret"
frame2_secret = "Frame2_Secret"

def verify_frame(frame_id, input_id, secret_text):
    # Переходимо до фрейму
    driver.switch_to.frame(frame_id)

    # Знаходимо поле введення і вводимо секретний текст
    input_field = driver.find_element(By.ID, input_id)
    input_field.send_keys(secret_text)

    # Натискаємо кнопку "Перевірити"
    button = driver.find_element(By.TAG_NAME, "button")
    button.click()

    # Чекаємо і зчитуємо текст сповіщення (alert)
    alert = driver.switch_to.alert
    alert_text = alert.text
    print(f"Alert text in {frame_id}: {alert_text}")

    # Перевірка результату верифікації
    if alert_text == "Верифікація пройшла успішно!":
        print(f"{frame_id} verification passed.")
    else:
        print(f"{frame_id} verification failed.")

    # Закриваємо сповіщення
    alert.accept()

    # Повертаємося до головного документа
    driver.switch_to.default_content()

# Виконуємо верифікацію для кожного фрейму
verify_frame("frame1", "input1", frame1_secret)
verify_frame("frame2", "input2", frame2_secret)

# Закриваємо браузер після завершення
driver.quit()




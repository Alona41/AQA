import requests
import os

# Визначення URL та параметрів запиту
url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {
    'sol': 1000,
    'camera': 'fhaz',
    'api_key': 'DEMO_KEY'
}

# Виконання запиту до API
response = requests.get(url, params=params)

# Перевірка статусу відповіді
if response.status_code == 200:
    data = response.json()
    photos = data.get('photos', [])

    # Перевірка, чи є фото
    if photos:
        # Створення директорії для збереження фото
        os.makedirs('mars_photos', exist_ok=True)

        # Завантаження і збереження фото
        for index, photo in enumerate(photos):
            photo_url = photo['img_src']
            img_response = requests.get(photo_url)

            if img_response.status_code == 200:
                # Формування імені файлу
                filename = f'mars_photos/mars_photo{index + 1}.jpg'
                with open(filename, 'wb') as img_file:
                    img_file.write(img_response.content)
                print(f'Збережено: {filename}')
            else:
                print(f'Не вдалося завантажити фото: {photo_url}')
    else:
        print('Не знайдено фото за заданими параметрами.')
else:
    print('Помилка при отриманні даних з API:', response.status_code)

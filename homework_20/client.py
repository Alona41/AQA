import requests

# URL базової адреси сервера
base_url = 'http://127.0.0.1:8080'


# 1. Завантаження зображення через POST /upload
def upload_image(file_path):
    with open(file_path, 'rb') as image_file:
        files = {'image': image_file}
        response = requests.post(f'{base_url}/upload', files=files)
        if response.status_code == 201:
            image_url = response.json()['image_url']
            print(f"Image uploaded successfully: {image_url}")
            return image_url
        else:
            print(f"Failed to upload image: {response.status_code}")
            return None


# 2. Отримання URL зображення через GET /image/<filename>
def get_image_url(filename):
    headers = {'Content-Type': 'text/plain'}
    response = requests.get(f'{base_url}/image/{filename}', headers=headers)
    if response.status_code == 200:
        image_url = response.url
        print(f"Image URL: {image_url}")
    else:
        print(f"Failed to get image URL: {response.status_code}")


# 3. Видалення зображення через DELETE /delete/<filename>
def delete_image(filename):
    response = requests.delete(f'{base_url}/delete/{filename}')
    if response.status_code == 200:
        message = response.json()['message']
        print(f"Image deleted: {message}")
    else:
        print(f"Failed to delete image: {response.status_code}")


# Використання функцій
if __name__ == '__main__':
    image_path = 'C:/Users/cluba/Pictures/_MG_3630.jpg'  # Шлях до зображення для завантаження
    uploaded_url = upload_image(image_path)

    if uploaded_url:
        filename = uploaded_url.split('/')[-1]  # Отримати ім'я файлу з URL
        get_image_url(filename)
        delete_image(filename)

import os
from json_helper import validate_json


import logging

logging.basicConfig(filename='json_your_second_name.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def validate_json_files(folder_path):

    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            validate_json(os.path.join(folder_path, filename))


if __name__ == "__main__":
    json_folder = 'C:/Users/cluba/OneDrive/Документы/work_with_json'
    validate_json_files(json_folder)

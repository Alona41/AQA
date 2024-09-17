from xml_helper import search_group_by_number
import logging

# Налаштування логера
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    xml_file = 'C:/Users/cluba/Downloads/groups.xml'
    group_number = '3'

    incoming_value = search_group_by_number(xml_file, group_number)

    if incoming_value:
        logging.info(f'Incoming value for group {group_number}: {incoming_value}')
    else:
        logging.info(f'Group {group_number} not found.')

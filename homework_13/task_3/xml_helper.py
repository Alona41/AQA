import xml.etree.ElementTree as ET


def search_group_by_number(xml_file, group_number):
    """
    Шукає групу за номером у XML-файлі і повертає значення 'incoming' для цієї групи.

    :param xml_file: шлях до XML-файлу
    :param group_number: номер групи для пошуку
    :return: значення 'incoming', якщо група знайдена, інакше None
    """
    tree = ET.parse(xml_file)
    root = tree.getroot()

    for group in root.findall('group'):
        number = group.find('number').text
        if number == group_number:
            return group.find('timingExbytes/incoming').text
    return None

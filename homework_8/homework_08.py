list_1: list[str] = ['1,2,3,4', '1,2,3,4,50', 'qwerty1,2,3']

def sum_all_charts_in_string_if_in(list_2: list[str]):
    result: list[int | str] = []  # Додаємо можливість мати строки в результатах
    for item in list_2:
        try:
            chars_list: list[str] = item.split(",")  # Задаємо тип елементів списку
            result.append(sum(int(integer) for integer in chars_list))
        except ValueError as exception:
            result.append(f"Не можу це зробити!: {exception}")
    print(result)

sum_all_charts_in_string_if_in(list_1)

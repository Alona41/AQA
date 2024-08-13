# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
# Initialize the appropriate variable
    multiplier = 1

# Complete the while loop condition.
    while multiplier > 0:
        result = number * multiplier

# десь тут помила, а може не одна
        if  result >= 25:
            break

        else:   # Enter the action to take if the result is greater than 25
             print(str(number) + "x" + str(multiplier) + "=" + str(result))


# Increment the appropriate variable
        multiplier += 1


multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел."""
def sum_number(numb_1,numd_2):
    numb = numb_1 + numd_2
    print(numb)
sum_number(3,5)


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""


def average_arithmetic(variable):
    print(sum(variable) / len(variable))


list_1 = [3, 4, 5]
average_arithmetic(list_1)

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""


def in_reverse_order(line):
    return line[::-1]


line_1 = "Hello world"
line_2 = in_reverse_order(line_1)
print(line_2)
# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку."""


def longest_word(list):
    list_2 = max(list, key=len)
    return list_2


inventory = ["банан", "фломастер", "ножиці"]
inventory_1 = longest_word(inventory)
print(inventory_1)

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""


def find_substring(str_1, str_2):
    str_3 = str_1.find(str_2)

    return str_3


str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))  # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))  # поверне -1

# task 7
"""Зробіть так, щоб кількість бананів була
 завжди в чотири рази більша, ніж яблук"""


def increase_in_bananas(appel):
    bannan = appel * 4
    print(bannan)


appels = 6
increase_in_bananas(appels)

# task 8
"""Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера."""


def amount_on_credit(month, cost):
    cost_1 = month * cost
    print(cost_1)


month_of_credit = 12
cost_month = 1500
amount_on_credit(month_of_credit, cost_month)
# task 9
"Виведіть, скількі разів у тексті зустрічається літера 'h'"


def number_of_letters(text, letter):
    count = 0
    for letter_1 in text:
        if letter_1 == letter:
            count += 1
    print(count)


text_1 = """ Polly,Molly and Dolly are three little girls. They live with their mother in a little house.
        Every day the girls' mother  works very much. But Polly, Molly and Dolly do not help her. They do not like to work."""
letter_2 = "l"
number_of_letters(text_1, letter_2)

# task 10
"""Виведіть, скільки слів у тексті починається з Великої літери?"""


def number_of_capitalized_words(text):
    count = 0
    letter_capilaze = text.split()
    for leters in letter_capilaze:
        if leters[0].isupper():
            count += 1
    print(count)


number_of_capitalized_words(text_1)
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
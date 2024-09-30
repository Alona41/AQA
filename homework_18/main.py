from generators import even_numbers, fibonacci
from iterators import ReverseIterator, EvenNumbersIterator
from decorators import log_args_and_result, exception_handler


print(list(even_numbers(10)))
print(list(fibonacci(10)))


my_list = [1, 2, 3, 4, 5]
for item in ReverseIterator(my_list):
    print(item)

for num in EvenNumbersIterator(10):
    print(num)


@log_args_and_result
def add(a, b):
    return a + b

add(3, 5)

@exception_handler
def divide(a, b):
    return a / b

print(divide(10, 2))
print(divide(10, 0))

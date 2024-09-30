

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def get_area(self):
        return self.__width * self.__height

    def get_perimeter(self):
        return 2 * (self.__width + self.__height)


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def get_area(self):
        return 3.14159 * (self.__radius ** 2)

    def get_perimeter(self):
        return 2 * 3.14159 * self.__radius

if __name__ == "__main__":
    shapes = [
        Rectangle(3, 4),
        Circle(5)
    ]

    for shape in shapes:
        print(f"Площа: {shape.get_area()}, Периметр: {shape.get_perimeter()}")

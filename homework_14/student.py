class Student:
    def __init__(self, first_name, last_name, age, average_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.average_grade = average_grade

    def update_average_grade(self, new_grade):
        self.average_grade = new_grade

    def get_info(self):
        return f"Ім'я: {self.first_name}, Прізвище: {self.last_name}, Вік: {self.age}, Середній бал: {self.average_grade}"



student = Student("Олена", "Коваль", 20, 4.5)


print(student.get_info())


student.update_average_grade(4.8)


print(student.get_info())

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Course, Student
import random

DATABASE_URL = 'sqlite:///student_system.db'


def init_db():
    # Створення бази даних
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)

    # Створення сесії
    Session = sessionmaker(bind=engine)
    session = Session()

    # Додавання курсів
    courses = ['Math', 'Science', 'History', 'Art', 'Computer Science']
    for course_name in courses:
        course = Course(name=course_name)
        session.add(course)

    # Додавання студентів
    students = []
    for i in range(1, 21):
        student = Student(name=f'Student {i}')
        students.append(student)
        session.add(student)

    session.commit()

    # Рандомне записування студентів на курси
    for student in students:
        enrolled_courses = random.sample(session.query(Course).all(), k=random.randint(1, 3))  # 1-3 курси
        student.courses.extend(enrolled_courses)

    session.commit()
    print("База даних ініційована, студенти та курси додані.")

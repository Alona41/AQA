from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Course, Student
from database import DATABASE_URL

def get_session():
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    return Session()

def add_student(name, course_name):
    session = get_session()
    new_student = Student(name=name)
    course = session.query(Course).filter_by(name=course_name).first()
    if course:
        new_student.courses.append(course)
        session.add(new_student)
        session.commit()
        print(f"Студента {name} успішно додано до курсу {course_name}.")
    else:
        print(f"Курс {course_name} не знайдено.")
    session.close()

def get_students_by_course(course_name):
    session = get_session()
    course = session.query(Course).filter_by(name=course_name).first()
    if course:
        students = [student.name for student in course.students]
    else:
        students = []
    session.close()
    return students

def get_courses_by_student(student_name):
    session = get_session()
    student = session.query(Student).filter_by(name=student_name).first()
    if student:
        courses = [course.name for course in student.courses]
    else:
        courses = []
    session.close()
    return courses

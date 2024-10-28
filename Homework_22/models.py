from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


# Таблиця для курсів
class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    students = relationship('Student', secondary='enrollments')


# Таблиця для студентів
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    courses = relationship('Course', secondary='enrollments')


# Таблиця для зв'язків між студентами та курсами
enrollments = Table('enrollments', Base.metadata,
                    Column('student_id', Integer, ForeignKey('students.id')),
                    Column('course_id', Integer, ForeignKey('courses.id'))
                    )

'''
engine
session
table
migrate
'''
from sqlalchemy import create_engine, Column, Integer, String,  or_, and_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/alchemy',echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    grade = Column(String(50))

# Base.metadata.create_all(engine)

'''
create instance of table class
add data to session
commit changes to database
'''

stu1 = Student(name='kalpesh',age=31,grade='engineer')
stu2 = Student(name='nikky',age=25,grade='developer')
stu3 = Student(name='sarang',age=25,grade='designer')
# session.add(stu1)
# session.add_all([stu2,stu3])
session.commit()

# -----get all data
# students = session.query(Student)
# for stu_info in students:
#     print('student : ', stu_info)

# ---------get data in order
# students = session.query(Student).order_by(Student.name)
# for stu_info in students:
#     print('student : ', stu_info.name)

# ------get data by filtering
# students = session.query(Student).filter(Student.name=='kalpesh').first()
# for stu_info in students:
#     print('student : ', stu_info.age)

# students = session.query(Student).filter(or_(Student.name == "nikky", Student.age == 25))
# for stu_info in students:
#     print('student : ', stu_info.grade)

# ------count of result
students = session.query(Student).filter(or_(Student.name == "kalpesh", Student.age == 25)).count()
# print('student : ', students)

# ###### update data ######

# ----- get the record
# students = session.query(Student).filter(Student.age==31).first()
# students.age = 29
# session.commit()

# ###### delete data ######

# ----- get the record
students = session.query(Student).filter(Student.age==29).first()
session.delete(students)
session.commit()

# ----- change value
# ----- commit change




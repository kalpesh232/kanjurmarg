# x = 'Hello' 
# y = 'Hello' 
# print(id(x))
# print(id(y))
# print(x is y)             # True

# a = [1, 2, 3]
# b = [1, 2, 3]
# print (a == b)              # true
# print(id(a))
# print(id(b))
# print (a is b)             # False

# print(0.1 + 0.2 == 0.3) 

# import math
# print(math.isclose(0.1 + 0.2, 0.3))  # This will return True
# print(0.1 + 0.2, 0.3)     # floating-point numbers like 0.1 and 0.2 cannot be exactly represented in binary

# ---------- Python has several built-in data types
# x = 10          # int
# y = 3.14        # float
# z = "Hello"     # str
# a = [1, 2, 3]   # list
# b = (1, 2, 3)   # tuple
# c = {"key": "value"}  # dict
# d = {1, 2, 3}   # set
# e = True        # bool
# f = None        # NoneType

# ---------- Tuples in Python have only a few built-in methods 
# tpl = (9,7,6,9,9,9,'k',3,7,6,'k')
# print(tpl.count('k'))
# print(len(tpl))
# print(tpl.index('k'))

# ---------- Can use a float value as a key in a dictionary
# my_dict = {
#     1.1 : 'kalpesh',
#     2.1 : 'h',
#     3.1 : 'shinde'
# }

# my_dict[2.1] = 'hvshinde'
# print(my_dict)
# print(my_dict[3.1])

# ---------- Join operations using Object-Relational Mapping (ORM) 
# # sqlalchemy.orm.declarative_base()
# from sqlalchemy.orm import declarative_base
# # from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import create_engine, Integer, String, ForeignKey, Column
# from sqlalchemy.orm import sessionmaker, relationship

# base = declarative_base()

# class Parent(base):
#     __tablename__ = 'parent'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(100))
#     child = relationship('Child', back_populates='parent')

# class Child(base):
#     __tablename__ = 'child'
#     id = Column(Integer, primary_key=True)
#     parent_id = Column(Integer, ForeignKey('parent.id'))
#     name = Column(String(100))
#     parent = relationship('Parent', back_populates='child')

# engine = create_engine('mysql+mysqlconnector://root:root@localhost/x')
# base.metadata.create_all(engine)
# Session = sessionmaker(bind=engine)
# session = Session()
# outerjoin
# result = session.query(Parent).join(Child).all()

# print('result : ', result)




###################################### DataFrame in Pandas ###############################################
# import pandas as pd

# data = {
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Age': [25, 30, 35],
#     'City': ['New York', 'Los Angeles', 'Chicago']
# }

# data = [
#     {'Name': 'Alice_lst', 'Age': 25, 'City': 'New York'},
#     {'Name': 'Bob_lst', 'Age': 30, 'City': 'Los Angeles'},
#     {'Name': 'Charlie_lst', 'Age': 35, 'City': 'Chicago'},
#     {'Name': 'kalpesh', 'Age': 31.5, 'City': None}
# ]

# df = pd.DataFrame(data, index=['a', 'b', 'c','d'])

# # print('----- head -----')
# # print(df.head())  # View the first few rows
# # print('----- tail -----')
# # print(df.tail())  # View the last few rows


# # print('----- Name -----')
# # print(df['Name'])          # Select a single column
# # print('----- Name,Age -----')
# # print(df[['Name', 'Age']]) # Select multiple columns
# # print('----- iloc -----')
# # print(df.iloc[0])          # Select a row by position
# # print('----- loc -----')
# # print(df.loc['a'])           # Select a row by index

# # print('------------------------------------')
# # print(df['Age'] > 25) 
# # print('----- Filtering Data -----')
# # print(df[df['Age'] > 25])  # Filter rows based on a condition

# df['Salary'] = [50000, 60000, 70000, 80000]  # Add a new column
# # df = df.fillna(0)          # Replace missing values with 0
# # df = df.dropna()           # Drop rows with missing values
# df = df.drop('Salary', axis=1)        # Remove a column
# # print( df)
# # print('----- shape -----')
# # print(df.shape)   # View the dimensions (rows, columns)
# # print('----- info -----')
# # print(df.info())  # View summary information
# # print('----- describe -----')
# # print(df.describe())  # View statistical summary

################################### merge two lists in Python #########################################

# list1 = [1, 2, 3]
# list2 = [4, 5, 1]

# # merged_list = list1 + list2

# # list1.extend(list2)
# # print(list1)

# merged_list = [item for sublist in (list1, list2) for item in sublist]
# for sublist in (list1, list2) :
#     for item in sublist : 
#         print('item : ', item)

# merged_list = [*list1, *list2]
# print(merged_list)

# import itertools
# merged_list = list(itertools.chain(list1, list2))
# print(merged_list)

# ########## Django sqlalchemy 

# '''
# engine
# session
# table
# migrate
# '''
# from sqlalchemy import create_engine, Column, Integer, String,  or_, and_
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base

# engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/alchemy',echo=False)
# Session = sessionmaker(bind=engine)
# session = Session()
# Base = declarative_base()

# class Student(Base):
#     __tablename__ = 'student'

#     id = Column(Integer, primary_key=True)
#     name = Column(String(50))
#     age = Column(Integer)
#     grade = Column(String(50))

# # Base.metadata.create_all(engine)

# '''
# create instance of table class
# add data to session
# commit changes to database
# '''

# stu1 = Student(name='kalpesh',age=31,grade='engineer')
# stu2 = Student(name='nikky',age=25,grade='developer')
# stu3 = Student(name='sarang',age=25,grade='designer')
# # session.add(stu1)
# # session.add_all([stu2,stu3])
# session.commit()

# # -----get all data
# # students = session.query(Student)
# # for stu_info in students:
# #     print('student : ', stu_info)

# # ---------get data in order
# # students = session.query(Student).order_by(Student.name)
# # for stu_info in students:
# #     print('student : ', stu_info.name)

# # ------get data by filtering
# # students = session.query(Student).filter(Student.name=='kalpesh').first()
# # for stu_info in students:
# #     print('student : ', stu_info.age)

# # students = session.query(Student).filter(or_(Student.name == "nikky", Student.age == 25))
# # for stu_info in students:
# #     print('student : ', stu_info.grade)

# # ------count of result
# # students = session.query(Student).filter(or_(Student.name == "kalpesh", Student.age == 25)).count()
# # print('student : ', students)

# # ###### update data ######

# # ----- get the record
# # students = session.query(Student).filter(Student.age==31).first()
# # students.age = 29
# # session.commit()

# # ###### delete data ######

# # ----- get the record
# # students = session.query(Student).filter(Student.age==29).first()
# # session.delete(students)
# # session.commit()

# ----- change value
# ----- commit change

# ---------- Concatenate 
# Strings
# result = "Hello" + " " + "World"  # "Hello World"
# # Lists
# result = [1, 2] + [3, 4]  # [1, 2, 3, 4]
# # ---------- Join 
# result = "-".join(["2024", "08", "16"])  # "2024-08-16"
# # ---------- Merge 
# import pandas as pd
# df1 = pd.DataFrame({'key': [1, 2, 3], 'A': ['A1', 'A2', 'A3']})
# df2 = pd.DataFrame({'key': [1, 2, 4], 'B': ['B1', 'B2', 'B4']})
# result = pd.merge(df1, df2, on='key')
# print(result)

########## Arguments in Python Functions
#---------- Positional Arguments:
# def greet(name, age):
#     print(f"Hello {name}, you are {age} years old.")

# greet("kalpesh", 30)

#---------- Keyword Arguments:
# def greet(name, age):
#     print(f"Hello {name}, you are {age} years old.")

# greet(age=30, name="kalpesh")

#---------- Default Arguments:
# def greet(name, age=25):
#     print(f"Hello {name}, you are {age} years old.")

# greet("kalpesh")  # Uses default age of 25
# greet("kalpesh",30)  

#---------- Variable-Length Arguments:
# def greet(*names):
#     for name in names:
#         print(f"Hello {name}")

# greet("kalpesh", "harishchandra", "shinde")

# def greet(**info):
#     for key, value in info.items():
#         print(f"{key}: {value}")

# greet(f_name="kalpesh", m_name='harishchandra', s_name="shinde")

#---------- Positional-Only and Keyword-Only Arguments:
# def greet(name, /, age):
#     print(f"Hello {name}, you are {age} years old.")

# greet("Alice", 25)  # Works
# greet(name="kalpesh", age=30)  # Error

# # def greet(name, *, age):
# #     print(f"Hello {name}, you are {age} years old.")

# # greet("kalpesh", age=30)  # Works
# # greet("Alice", 25)  # Error

# ---------- List comprehension in Python

# x = [x*2 for x in range(10) if x%2 == 0]
# print('x : ', x)


# --------- Inheritance

### 1. **Single-Level Inheritance**:
# In single-level inheritance, a child class inherits from a single parent class.
# class Animal:
#     def speak(self):
#         print("Animal speaks")

# class Dog(Animal):  # Single-level inheritance (Dog inherits from Animal)
#     def bark(self):
#         print("Dog barks")

# dog = Dog()
# dog.speak()  # Inherited from Animal
# dog.bark()   # Defined in Dog


### 2. **Multi-Level Inheritance**:
# In multi-level inheritance, a class inherits from a parent class, and another class inherits from that

# class Animal:
#     def speak(self):
#         print("Animal speaks")

# class Dog(Animal):  # Dog inherits from Animal
#     def bark(self):
#         print("Dog barks")

# class Puppy(Dog):  # Puppy inherits from Dog (which inherits from Animal)
#     def weep(self):
#         print("Puppy weeps")

# puppy = Puppy()
# puppy.speak()  # Inherited from Animal
# puppy.bark()   # Inherited from Dog
# puppy.weep()   # Defined in Puppy


### 3. **Multiple Inheritance**:
# In multiple inheritance, a class can inherit from more than one parent class.

# class Mammal:
#     def has_fur(self):
#         print("Mammal has fur")

# class Bird:
#     def lay_eggs(self):
#         print("Bird lays eggs")

# class Bat(Mammal, Bird):  # Multiple inheritance (Bat inherits from both Mammal and Bird)
#     def fly(self):
#         print("Bat flies")

# bat = Bat()
# bat.has_fur()    # Inherited from Mammal
# bat.lay_eggs()   # Inherited from Bird
# bat.fly()        # Defined in Bat

# ### 4. **Hybrid Inheritance**:
# # Hybrid inheritance is a combination of two or more types of inheritance (like multiple and multi-level inheritance).

# class Vehicle:
#     def move(self):
#         print("Vehicle moves")

# class Car(Vehicle):
#     def drive(self):
#         print("Car drives")

# class Boat(Vehicle):
#     def sail(self):
#         print("Boat sails")

# class AmphibiousCar(Car, Boat):  # Hybrid inheritance (inherits from both Car and Boat)
#     def switch_mode(self):
#         print("AmphibiousCar switches between driving and sailing")

# amphibious_car = AmphibiousCar()
# amphibious_car.move()         # Inherited from Vehicle
# amphibious_car.drive()        # Inherited from Car
# amphibious_car.sail()         # Inherited from Boat
# amphibious_car.switch_mode()  # Defined in AmphibiousCar


### 5. **Hierarchical Inheritance**:
# In hierarchical inheritance, multiple child classes inherit from a single parent class.

# class Animal:
#     def speak(self):
#         print("Animal speaks")

# class Dog(Animal):  # Dog inherits from Animal
#     def bark(self):
#         print("Dog barks")

# class Cat(Animal):  # Cat also inherits from Animal
#     def meow(self):
#         print("Cat meows")

# dog = Dog()
# dog.speak()  # Inherited from Animal
# dog.bark()   # Defined in Dog

# cat = Cat()
# cat.speak()  # Inherited from Animal
# cat.meow()   # Defined in Cat

# -------- Reverse a String
# Input = "Python"
# output = Input[::-1]
# print(output)

# -------- Count Occurrences of a Character in a String
# Input= "hello world"
# x = 'o'
# counter = 0
# for i in Input:
#     if x == i :
#         counter += 1
# print(counter)

# -------- First Non-Repeating Character in a String
# x = "swiss"
# from collections import Counter
# r = Counter(x)
# for i, j in r.items():
#     if j == 1 :
#         print('r : ', i, 'j : ', j)
#         break

# -------- Capitalize First Letter of Each Word
# Input= "hello world"
# print(Input.title())

# -------- Remove Duplicate Characters from a String
# Input = "programming"
# mystr = ''.join(dict.fromkeys(Input))
# print(mystr)

# -------- Check if Two Strings are Anagrams
# String_1= "listenlpw"
# String_2 = "silentlpr"
# print(sorted(String_1) == sorted(String_2))

# -------- Replace Spaces with '%20' in a String
# Input= "hello world"
# x = Input.replace(' ', '%20')
# print(x)

# -------- Find Longest Common Prefix in a List of Strings
# Longest common same words
# Input= ["flooer", "floo", "flooht"]
# main_str = ''
# for i in zip(*Input):
#     if len(set(i)) == 1:
#         main_str += i[0]
# print(main_str)

# -------- Check if All Characters in a String are Unique
# Input = "abcde"
# st = set(Input)
# if len(Input) == len(st):
#     print('True')
# else:
#     print('false')

# -------- Find the Most Frequent Character in a String
# Input = "bwanwanwaxwxxw"
# from collections import Counter
# x = Counter(Input)
# for k,v in x.items():
#     if v == max(x.values()):
#         print(k, ':', v)

# -------- Rotate a String by 'n' Characters
# Input =  "abcdef"
# result = ''
# x = 3
# result +=  Input[x:] + Input[:x]
# print(result)

# -------- Sum of All Numbers in a Mixed Alphanumeric String
# Input = "abc123xyz45"
# num = ['7','8','9','4','5','6','1','2','3','0']
# ls = []
# x1 = ''
# for i in Input:
#     # print('i : ', i)
#     if i in num:
#         x1 += i
#     else:
#         if x1 != '':
#             x1 = int(x1)
#             ls.append(x1)
#         x1 = ''
#     # print('x : ', ls)
#     # x1 = ''
# x1 = int(x1)
# ls.append(x1)
# print((sum(ls)))

# -------- Run-Length Encoding (RLE) Compression
# Input =  "aaabbc"
# from collections import Counter
# mystr = ''
# x = Counter(Input)
# for i,j in x.items():
#     mystr += i + str(j)
# print(mystr)

# -------- Generate and Sort All Substrings of a String
Input = "abc"
s = []
for i in range(len(Input)):
    for j in range(i,len(Input)):
        s.append(Input[i:j+1])
print(s)
temmp = None
for i in range(len(s)):
    for j in range(len(s)):
        if len(s[i]) < len(s[j]):
            temmp = s[i]
            s[i] = s[j]
            s[j] = temmp
print(s)














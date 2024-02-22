# pip install pymysql
import pymysql

def createConn():
    try :
        conn = pymysql.connect(
            host = "localhost",
            database = "crud_database",
            user = "root",
            password = "root",
            port = 3306
        )

        print("Connection Eshtablishes")
        return conn
    except Exception as e :
        print("Connection Not Eshtablishes : ", str(e))

def createTable():
    try:
        conn = createConn()
        query = "create table students (sid int primary key auto_increment ,name varchar(50) ,email varchar(50) ,city varchar(50))"
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        print("table created")
    except Exception as e:
        print("table not created : ", str(e))

# createTable()

def insertTable(name,email,city):
    try:
        conn = createConn()
        query = f"insert into students(name, email, city) values ('{name}','{email}','{city}')"
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        print('data inserted')
        conn.close()
    except Exception as e:
        print('data not inserted : ', str(e))

# name = input('Enter Name : ')
# email = input('Enter Email : ')
# city = input('Enter city : ')
# insertTable(name, email,city)
        
def fetchData():
# def fetchData(sid):
    try:
        conn = createConn()
        query = "select * from students"
        # query = f"select * from students where sid = {sid}"
        cur = conn.cursor()
        cur.execute(query)
        result = cur.fetchall()
        for i in result:
            print(i)
        conn.commit()
        conn.close()
    except Exception as e:
        print("can't fetch data : ", str(e))
# id = int(input('Enter Student ID : '))
# fetchData()
# fetchData(id)
        
def updateData(name,email,city,sid):
    try:
        conn = createConn()
        query = f"update students set name = '{name}', email='{email}', city='{city}' where sid = {sid}"
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        print('data updated')
        conn.close()
    except  Exception as e:
        print('Error while Updating : ', str(e))

# fetchData()

# name = input('Enter Name : ')
# email = input('Enter Email : ')
# city = input('Enter city : ')
# id = int(input('Enter ID : '))
# updateData(name, email,city,id)

# fetchData()
        
def deleteDate(sid):
    try:
        conn = createConn()
        query = f"delete from students where sid = {sid}"
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        print('data deleted')
    except Exception as e:
        print('Error while Deleting : ', str(e))
fetchData()

id = int(input('Enter ID : '))
deleteDate(id)

fetchData()
        



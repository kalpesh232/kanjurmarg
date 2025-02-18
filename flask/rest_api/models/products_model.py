import mysql.connector
import json
from flask import make_response
import jwt
from datetime import datetime, timedelta

class user_model:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host="localhost", user="root", password = "root", database="rest_api")
            self.conn.autocommit = True
            self.cur =  self.conn.cursor(dictionary=True)
        except:
            print('some error')
    def user_signup_model(self):
        self.cur.execute("select * from users ")
        result1 = self.cur.fetchall()
        if len(result1) > 0 :
            # result = json.dumps(result1)
            result = result1
            # print('Len :', len(result))
            # print('Type :', type(result))
            # print('result :', result)
          
            # return  result
            res = make_response({"payload" : result}, 200)
            # print('res :', res)
            res.headers['Access-Control-Allow-Origin'] = "*"
            return  res
        else:
            return  make_response({"message" :  "No Data Found"}, 204)
        
    def user_addone_model(self, mydata):
        # self.cur.execute("select * from users")
        print('request.form : ',  mydata)
        self.cur.execute(f"insert into users (name,email,phone,role,password) values ('{mydata['name']}','{mydata['email']}','{mydata['phone']}','{mydata['role']}','{mydata['password']}')")
        # print('request.form : ',  query)
        return make_response( {"message" : "User created successfully"}, 200)
    
    def user_update_model(self, mydata):
        print('request.form : ',  mydata)
        self.cur.execute( f"UPDATE users SET name = '{mydata['name']}', email = '{mydata['email']}', phone = '{mydata['phone']}', role = '{mydata['role']}', password = '{mydata['password']}' WHERE id = {mydata['id']}")
        if self.cur.rowcount > 0:
            return  make_response({"message" : "User updated successfully !"}, 200)
            # return  "User updated successfully"
        else:
            return  make_response({"message" : "Nothing To Updated"}, 202)
        
    def user_delete_model(self, mydata):
        print('request.form : ',  mydata)
        self.cur.execute( f"Delete from  users WHERE id = {mydata}")
        if self.cur.rowcount > 0:
            return make_response( {"message" : "User deleted successfully"}, 200)
        else:
            return  make_response({"message" : "Nothing To Delete"}, 202)
        
    def user_update_with_patch_model(self, mydata, id):
        query = "UPDATE users SET "
        for key in mydata:
            query +=  f'{key} = "{mydata[key]}",'
        query = query[:-1] + f" WHERE id = {id}"
        self.cur.execute( query)
        if self.cur.rowcount > 0:
            return  make_response({"message" : "User updated successfully !"}, 200)
            # return  "User updated successfully"
        else:
            return  make_response({"message" : "Nothing To Updated"}, 202)
        
    def user_pagibation_model(self, limit, page):
        limit = int(limit)
        page = int(page)
        start = (limit * page) - limit
        print('start > ' , start)
        self.cur.execute( f"Select * from users limit {start} , {limit}")
        result = self.cur.fetchall()
        print('result > ' , result)
        if len(result) > 0 :
            res = make_response({"payload" : result, "page":page, "limit" : limit}, 200)
            return  res
        else:
            return  make_response({"message" :  "No Data Found"}, 204)
        
    def user_update_avatar_file_model(self, avtar, id):
        query = f"UPDATE users SET avatar = ' {avtar}' where id = {id}"
        self.cur.execute( query)
        if self.cur.rowcount > 0:
            return  make_response({"message" : "File Uploaded successfully !"}, 201)
            # return  "User updated successfully"
        else:
            return  make_response({"message" : "Nothing To Updated"}, 202)
        
    def user_login_model(self,user_info):
        self.cur.execute(f"select id,name,email,avatar, roles, phone from users where email = '{user_info['email']}' and password =  '{user_info['passsword']}' ")
        result1 = self.cur.fetchall()
        if len(result1) > 0 :
            user_date = result1[0]
            exp_time =  datetime.now() + timedelta( minutes= 15)
            exp_epoch_time = exp_time.timestamp()
            payload = {
                "payload" : user_date,
                "exp" : exp_epoch_time
            }
            jwt_token = jwt.encode(payload,'secret',algorithm="HS256")
            print(int(exp_epoch_time))
            # return  result1
            # return  str(result1)
            return  make_response({'payload' : jwt_token}, 200)
        else:
            return  make_response({"message" :  "No Data Found"}, 204)
        
    def user_multiple_model(self, mydata):
        # self.cur.execute("select * from users")
        qury = "insert into users (name,email,phone,role,password) values "
        for data in mydata:
            qury +=f" ('{data['name']}','{data['email']}','{data['phone']}',{data['role']},'{data['password']}')"
        final_query = qury.rstrip(qury)
        print('datae ', final_query)
        self.cur.execute(final_query)
        return make_response( {"message" : "Multiple User created successfully"}, 201)
    
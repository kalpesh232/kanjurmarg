from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api 
from flask_jwt_extended import create_access_token, JWTManager, jwt_required, get_jwt_identity

app = Flask(__name__)
app.config['SECRET_KEY'] = 'G@W:b_k#w|A1.C3.E8.L2.S9.V2.X4.Z7'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/eavhdi'

db = SQLAlchemy(app)
api = Api(app)
jwt = JWTManager(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), unique=True, nullable= False)
    password = db.Column(db.String(100), nullable= False)

with app.app_context():
    db.create_all()

class userRegister(Resource):
    def post(self):
        data = request.get_json()
        username = data['username']
        password = data['password']

        if not username or not password:
            return {'message' : 'UserName or Passsword Missing'}, 400
        if User.query.filter_by(username=username).first():
            return {'message' : "UserName already Exist"}, 400
        
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return {'message' : 'User created Successfully'}, 200
    
class userLogin(Resource):
    def post(self):
        data = request.get_json()
        username = data['username']
        password = data['password']

        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            access_token = create_access_token(identity= user.id)
            return {'access_token' : access_token}, 200
        return {'message' : "Invalid Credentials"}, 401
    
class protectResource(Resource):
    @jwt_required()
    def get(self):
        current_user_id = get_jwt_identity()
        return {"message" : f"Hello user {current_user_id}, you accessed the protected resource"}
        
api.add_resource(userRegister,'/register')
api.add_resource(userLogin,'/login')
api.add_resource(protectResource, '/secure')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
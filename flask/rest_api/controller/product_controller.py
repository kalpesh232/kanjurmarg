
from app import app
from models.products_model import user_model
from models.auth_model import auth_model
from flask import request, send_file
from datetime import datetime
import os

obj = user_model()
auth = auth_model()

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/get_all')
@auth.token_authorization()
def product():
    # return "product"
    return obj.user_signup_model()

@app.route('/addone', methods=['POST'])
def addone():
    # return "product"
    return obj.user_addone_model(request.form)

@app.route('/update', methods=['PUT'])
def update():
    # return "product"
    print('request.form : ', request.form)
    return obj.user_update_model(request.form)

# @app.route('/delete', methods=['DELETE'])
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    # return "product"
    myid = id
    print('myid ................: ', myid)
    return obj.user_delete_model(myid)

@app.route('/update_with_patch/<int:id>', methods=['PATCH'])
def update_with_patch(id):
    # return "product"
    print('request.form : ', request.form,id)                       
    return obj.user_update_with_patch_model(request.form,id)

@app.route('/pagination/<int:limit>/<int:page>', methods=['GET'])
def pagination(limit,page):
    return obj.user_pagibation_model(limit,page)

@app.route('/upload_file/<int:id>', methods=['PUT'])
def upload_file(id):
    file = request.files['avatar']
    FileNaneSplit = file.filename.split('.')
    FileExt = FileNaneSplit[len(FileNaneSplit) - 1]
    uniqueFileName = str( datetime.now().timestamp()).replace('.','')
    FinefileName = uniqueFileName + '.' +FileExt
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], FinefileName)
    print('='*153, file_path)
    file.save(file_path)
    return  obj.user_update_avatar_file_model(FinefileName, id)

@app.route('/uploads/<filename>')
def read_uploaded_file(filename):
    # Construct the path to the uploaded file
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    return send_file(file_path) 

@app.route('/login', methods=['POST'])
def user_login_controller():
    return obj.user_login_model(request.form)

@app.route('/add_multiple', methods=['POST'])
def add_multiple():
    # return "product"
    return obj.user_multiple_model(request.json)


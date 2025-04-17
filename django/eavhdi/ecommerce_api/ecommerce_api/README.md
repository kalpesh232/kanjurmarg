pip install djangorestframework
django-admin startproject ecommerce_api
cd ecommerce_api
python manage.py startapp products
pip install mysqlclient
pip install pymysql
pip install cryptography



settings --- INSTALLED_APPS
          |- urls  
          |-DATABASES 

models > serializers > views > urls

python manage.py makemigrations
python manage.py migrate

import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY',  '1k3a8l12p19e22s24h27')
    SQLALCHEMY_DATABASE_URI =  "mysql+pymysql://root:root@localhost:3306/klvhr_ax"
    SQLALCHEMY_TRACK_MODIFICATION = False
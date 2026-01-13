import os 

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', '1K3A8L12P19E22S24H27')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
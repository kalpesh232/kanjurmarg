import os 

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', '1k3a8l12p19e22s24h27')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
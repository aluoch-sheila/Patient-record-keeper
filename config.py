import os

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://odipo:110P05124hh@localhost/patient'



class ProdConfig(Config):
    '''
    production configurations child class
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    '''
    development configuration child class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://odipo:110P05124hh@localhost/patient'

    DEBUG = True

config_options = {
 'development': DevConfig,
 'production': ProdConfig,
 # 'test':TestConfig
 }

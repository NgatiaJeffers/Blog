import os 

class Config:
    '''
    General configuration parent Class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    RANDOM_QUOTE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'

    # DATABASE configuration
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:Access@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # UPLOAD IMG configuration
    UPLOAD_PHOTOS_DEST = 'app/static/photos'

    # EMAIL Configuration
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'jeffersongakuya@gmail.com'
    MAIL_PASSWORD = 'jifewry4f438fshdf8898'

    # SIMPLE MDE configuration
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
    '''
    Production configuration Child Class

    Args:
        Config: The parent configuration class with General Configuration settigs
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config: The parent configuration class with General Configuration Settings
    '''
    

class TestConfig(Config):
    '''
    Testing Configuration Child Class

    Args:
        Config: The parent Configuration Class with General Configuration Settings
    '''

    pass

    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'TestConfig': TestConfig
}
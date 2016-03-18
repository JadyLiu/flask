import os

# default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = '2e~\x97\x99\x0f\x88 \x83\xab]\xc4O\x8d\xefAq\xb1\x8bGvh\x97\x08'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False
    
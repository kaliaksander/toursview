import os

# defauls config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = 'y\xfe\x0e\x92\xbd\xa8$\xcb\x18j\xe1\xe82\x10A\xf9T\xd2\x87\xda,\x95\x8e\xad'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///posts.db'


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False

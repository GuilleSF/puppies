import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	DEBUG = False
	TESTING = False
	CSRF_ENABLED = True
	SECRET_KEY = 'p\xa0\xfc\xc9\x16\xea\xb5\xcc\x8b>r3f\xa8c\x9f\xb3\xdc\xa9\x91H\xe5/3'

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestConfig(Config):
	DEBUG=True
	CACHE_TYPE='null'
	MAIL_SERVER='localhost'
	
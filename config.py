class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://sammy:6660sS!x@localhost/flask_app_test'
    SECRET_KEY = 'something very secret'
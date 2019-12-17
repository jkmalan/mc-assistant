from os import path

dir_db = path.join(path.dirname(path.abspath(__file__)), '../sql')


class Config(object):
    # PROJECT SETTINGS
    SECRET_KEY = 'MicroCenterSecretKey'

    # DATABASE SETTINGS
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(dir_db, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # MAIL SETTINGS
    MAIL_USE_SSL = True
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465

    # GOOGLE SETTINGS
    GOOGLE_ACCESS_KEY = ''
    GOOGLE_USER_AGENT = ''

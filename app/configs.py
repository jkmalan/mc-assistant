from os import path, getenv

DATABASE_DIR = path.join(path.dirname(path.abspath(__file__)), '../sql')


class Config(object):
    # CUSTOM SETTINGS
    DATABASE_TYPE = getenv('MF_DATABASE_TYPE', 'sqlite')
    DATABASE_HOST = getenv('MF_DATABASE_HOST', 'localhost')
    DATABASE_PORT = getenv('MF_DATABASE_PORT', '3306')
    DATABASE_NAME = getenv('MF_DATABASE_NAME', 'microcenter')
    DATABASE_USER = getenv('MF_DATABASE_USER', 'microcenter')
    DATABASE_PASS = getenv('MF_DATABASE_PASS', 'microcenter')
    DATABASE_MYSQL = 'mysql+mysqldb://' \
                     + DATABASE_USER + ':' \
                     + DATABASE_PASS + '@' \
                     + DATABASE_HOST + ':' \
                     + DATABASE_PORT + '/' \
                     + DATABASE_NAME
    DATABASE_SQLITE = 'sqlite:///' + path.join(DATABASE_DIR, 'app.db')

    # FLASK SETTINGS
    SECRET_KEY = getenv('MF_SECRET_KEY', 'ThisKeyIsSuperSecret')

    # DATABASE SETTINGS
    SQLALCHEMY_DATABASE_URI = DATABASE_MYSQL if DATABASE_TYPE == 'mysql' else DATABASE_SQLITE
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # MAIL SETTINGS
    MAIL_USE_SSL = True
    MAIL_USERNAME = getenv('MF_MAIL_USER', 'microcenter')
    MAIL_PASSWORD = getenv('MF_MAIL_PASS', 'microcenter')
    MAIL_SERVER = getenv('MF_MAIL_HOST', 'smtp.gmail.com')
    MAIL_PORT = getenv('MF_MAIL_PORT', '465')

    # GOOGLE SETTINGS
    GOOGLE_ACCESS_KEY = ''
    GOOGLE_USER_AGENT = ''

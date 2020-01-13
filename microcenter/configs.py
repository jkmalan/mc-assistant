from os import path, getenv

DATABASE_DIR = path.join(path.dirname(path.abspath(__file__)), '../databases')


class Config(object):
    # CUSTOM SETTINGS
    DATABASE_TYPE = 'sqlite'
    DATABASE_SQLITE = 'sqlite:///' + path.join(DATABASE_DIR, 'microcenter.db')
    DATABASE_MYSQL = 'mysql+mysqldb://' \
                     + getenv('MF_DATABASE_USER', 'microcenter') + ':' \
                     + getenv('MF_DATABASE_PASS', 'microcenter') + '@' \
                     + getenv('MF_DATABASE_HOST', 'localhost') + ':' \
                     + getenv('MF_DATABASE_PORT', '3306') + '/' \
                     + getenv('MF_DATABASE_NAME', 'microcenter')

    # FLASK SETTINGS
    SECRET_KEY = getenv('MF_SECRET_KEY', 'ThisKeyIsSuperSecret')

    # DATABASE SETTINGS
    SQLALCHEMY_DATABASE_URI = DATABASE_MYSQL if DATABASE_TYPE == 'mysql' else DATABASE_SQLITE
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # GOOGLE SETTINGS
    GOOGLE_ACCESS_KEY = ''
    GOOGLE_USER_AGENT = ''

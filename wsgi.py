from microcenter import create_app

application = create_app()

from os import path

application_path = path.abspath(path.dirname(__file__))

from sys import path

path.insert(0, application_path)

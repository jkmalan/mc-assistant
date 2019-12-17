from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail

from app.configs import Config
config = Config()

db = SQLAlchemy()
lm = LoginManager()
mx = Mail()


def create_app():
    app = Flask(__name__)

    app.config.from_object(config)

    db.init_app(app)
    lm.init_app(app)
    mx.init_app(app)

    # Register routes
    from app.route import dash, site
    app.register_blueprint(dash)
    app.register_blueprint(site)

    # Prepare assets directory
    app.static_folder = '../web/static'

    # Prepare database
    from app.main import models
    with app.app_context():
        db.create_all()

    # Prepare login manager
    lm.login_view = 'site.signin'

    return app

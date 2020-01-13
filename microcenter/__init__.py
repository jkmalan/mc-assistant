from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from microcenter.configs import Config
config = Config()

db = SQLAlchemy()
lm = LoginManager()


def create_app():
    app = Flask(__name__)

    app.config.from_object(config)

    db.init_app(app)
    lm.init_app(app)

    # Register routes
    from microcenter.views.anonymous import anonymous_bp
    app.register_blueprint(anonymous_bp)
    from microcenter.views.associate import associate_bp
    app.register_blueprint(associate_bp, url_prefix='/a')
    from microcenter.views.manager import manager_bp
    app.register_blueprint(manager_bp, url_prefix='/m')

    # Prepare assets directory
    app.template_folder = '../templates'
    app.static_folder = '../static'

    # Prepare database
    with app.app_context():
        db.create_all()

    # Prepare login manager
    lm.login_view = 'anonymous.signin'

    return app

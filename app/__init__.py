from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#from flask_seasurf import SeaSurf

db = SQLAlchemy()

migrate = Migrate()

#csrf = SeaSurf()

def create_app(config=None):
    app = Flask(__name__)

    #csrf.init_app(app)

    app.debug = True

    # hier zou je dan de juiste config nemen(zie google meet file)
    app.config.from_object('configuration.BaseConfiguration')

    db.init_app(app)

    do_register_blueprint(app)
    do_register_error_handlers(app)

    migrate.init_app(app, db)
    return app


def do_register_blueprint(flaskapp):
    from app.bp_general import bp_general
    from app.bp_user import bp_user
    from app.bp_backlash import bp_backlash

    flaskapp.register_blueprint(bp_general)
    flaskapp.register_blueprint(bp_user)
    flaskapp.register_blueprint(bp_backlash)

def do_register_error_handlers(flaskapp):
    pass
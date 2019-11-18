import os
from flask import Flask
from .models import db
from flask_migrate import Migrate
from .views import web
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))
migrate = Migrate()

def create_app():
    """Create Flask app."""
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'hard to guess string'
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(web)
    return app

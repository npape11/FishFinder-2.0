from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

db = SQLAlchemy()

def create_app():

    load_dotenv()

    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv("SEC_KEY")
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DB_URI")
    db.init_app(app)

    from .auth import auth
    from .views import views

    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(views, url_prefix='/')

    from .models import users

    with app.app_context():
        db.create_all()

    return app

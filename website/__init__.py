from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

db = SQLAlchemy()
load_dotenv()

def create_app():

    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv("SEC_KEY")
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DB_URI")
    db.init_app(app)

    from .auth import auth

    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User

    return app

print(os.getenv("SEC_KEY"))
print(os.getenv("DB_URI"))

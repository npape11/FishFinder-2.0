from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_login import LoginManager
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

    from .models import Users, FishSpecies, Catches
    from .seed import seed_fish_species
    
    with app.app_context():
        
        db.create_all()

        if not FishSpecies.query.first():
            seed_fish_species()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return Users.query.get(int(id))

    return app

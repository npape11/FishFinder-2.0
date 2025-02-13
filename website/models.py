from flask_login import UserMixin
from datetime import datetime
from . import db

class Users(db.Model, UserMixin):
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class FishSpecies(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    scientific_name = db.Column(db.String(255), nullable=False)
    habitat = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=False)

    catches_fishSp = db.relationship('Catches', backref='fish_species', lazy=True)

class Catches(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    species_id = db.Column(db.Integer, db.ForeignKey('fish_species.id', ondelete="CASCADE"), nullable=False)
    weight = db.Column(db.Float, nullable=False)
    length = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.now)
    
    user_Catches = db.relationship('Users', backref='catches', lazy=True)


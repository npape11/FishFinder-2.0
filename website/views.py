from flask import Flask, Blueprint, render_template, request, redirect, url_for
from . import db
from .models import FishSpecies

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('base.html')

@views.route('/fish')
def fish_species():
    fish_cards = FishSpecies.query.all()
    return render_template('fish_cards.html', fish_cards=fish_cards)

@views.route('/fish/<int:fish_id>')
def fish_details(fish_id):
    fish = FishSpecies.query.get_or_404(fish_id)  # Fetch fish by ID or return 404 if not found
    return "fish id"

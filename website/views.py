from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from .models import Users, FishSpecies, Catches
from . import db

views = Blueprint('views', __name__)

#Home Route

@views.route('/')
@login_required
def home():
    return render_template('base.html', user=current_user)

#Catch Route

@views.route('/submit-catch', methods=('GET','POST'))
@login_required
def submit_catch():
    if request.method == 'POST':
        
        species_id = request.form.get('species_id')
        weight = request.form.get('weight')
        length = request.form.get('length')
        latitude = request.form.get('latitude')
        longitude = request.form.get('longitude')
        
        if not (species_id and weight and length and latitude and longitude):
            flash('Please fill out all fields.', category='error')
            return redirect(url_for('views.submit_catch'))

        new_catch = Catches(
            user_id=current_user.id,  # Automatically associate with logged-in user
            species_id=species_id,
            weight=weight,
            length=length,
            latitude=latitude,
            longitude=longitude
        )

        db.session.add(new_catch)
        db.session.commit()
        flash('Catch successfully recorded!', category='success')
        return redirect(url_for('views.home'))
    
    fish_species = FishSpecies.query.all()
    return render_template('submit_catch.html', fish_species=fish_species, user=current_user)

#Fish Species/Information Routes

@views.route('/fish')
@login_required
def fish_species():
    fish_cards = FishSpecies.query.all()
    return render_template('fish_cards.html', fish_cards=fish_cards, user=current_user)

@views.route('/fish/<int:fish_id>')
@login_required
def fish_details(fish_id):
    fish = FishSpecies.query.get_or_404(fish_id)  # Fetch fish by ID or return 404 if not found
    return "fish id"

#Profile/User Routes

@views.route('/<string:user_username>')
@login_required
def profile(user_username):
    user = Users.query.get_or_404(user_username)
    return "User exists"

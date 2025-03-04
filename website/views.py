from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash, abort
from flask_login import login_user, login_required, logout_user, current_user
from .models import Users, FishSpecies, Catches
from . import db
from dotenv import load_dotenv
import os, requests

views = Blueprint('views', __name__)

#Home Route
@views.route('/')
@login_required
def home():
    
    # Fetch all catches
    recent_catches = db.session.query(
        Catches,  # Selects all columns from Catches
        Users.username,
        FishSpecies.name
    ).join(Users, Catches.user_id == Users.id) \
    .join(FishSpecies, Catches.species_id == FishSpecies.id) \
    .order_by(Catches.timestamp.desc()) \
    .limit(10).all()
    print(recent_catches)
    # Fetch only user's catches
    user_catches = Catches.query.filter_by(user_id=current_user.id).order_by(Catches.timestamp.desc()).all()

    return render_template("home.html", user=current_user, username=current_user.username, recent_catches=recent_catches, user_catches=user_catches)

#Catch Route
@views.route("/log-catch", methods=["GET", "POST"])
@login_required
def log_catch():

    load_dotenv()
    api_key = os.getenv("GOOGLE_MAPS_API_KEY")

    if request.method == "POST":
        #Form for logging a new catch
        species_id = request.form.get("species_id")
        weight = request.form.get("weight")
        length = request.form.get("length")
        latitude = request.form.get("latitude")
        longitude = request.form.get("longitude")
        address = geocode(latitude, longitude)

        #Enforcing values
        if not latitude or not longitude:
            flash("Please select a location on the map!", category="error")
            return redirect(url_for("views.log_catch"))
        elif not species_id and weight and length:
            flash("All fields must be filled out!", category="error")
            return redirect(url_for("views.log_catch"))
        
        #Creating a new catch for Catches table
        new_catch = Catches(
            user_id=current_user.id,
            species_id=species_id,
            weight=weight,
            length=length,
            latitude=latitude,
            longitude=longitude,
            address=address
        )

        db.session.add(new_catch)
        db.session.commit()

        flash("Catch submitted successfully!", "success")
        return redirect(url_for("views.home"))

    fish_species = FishSpecies.query.all()
    return render_template("log_catch.html", user=current_user, fish_species=fish_species, api_key=api_key)

#Fish Species/Information Routes
@views.route('/fish')
@login_required
def fish_species():
    fish_cards = FishSpecies.query.all()
    return render_template('fish_cards.html', fish_cards=fish_cards, user=current_user)

@views.route('/fish/<int:fish_id>')
@login_required
def fish_details(fish_id):
    fish = FishSpecies.query.filter_by(id=fish_id).first()  # Fetch fish by ID or return 404 if not found
    if fish is None:
        abort(404)
    return "fish id"

#Profile/User Routes
@views.route('/<string:username>')
@login_required
def profile(username):
    userProfile = Users.query.filter_by(username=username).first()
    if userProfile is None:
        abort(404)
    return render_template('profile.html', user=current_user, userProfile=userProfile)

#Proxy route for Google Maps API call
def geocode(lat, lng):
    load_dotenv()
    api_key = os.getenv("GOOGLE_MAPS_API_KEY")
    url = f'https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lng}&key={api_key}'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'OK':
            
            city = None
            state = None
            country = None

            for result in data['results']:
                address_components = result['address_components']
                for component in address_components:
                    if "locality" in component["types"]:
                        city = component["long_name"]
                    if "administrative_area_level_1" in component["types"]:
                        state = component["short_name"]  # Use "long_name" if you want full state name
                    if "country" in component["types"]:
                        country = component["long_name"]
            if city and state:
                cityState=f"{city}, {state}"
                return cityState
            if state and country:
                stateCountry=f"{state}, {country}"
                return stateCountry
            if country:
                return country
        else:
            return None
    else:
        print(f"Error: Unable to connect to the Google Maps API (Status Code: {response.status_code})")
        return None


from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from .models import Users
from . import db
import re

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=('GET', 'POST'))
def register():

    if current_user.is_authenticated:  # Check if the user is already logged in
        return redirect(url_for('views.home'))

    if request.method == 'POST':

        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        repeat_pass = request.form.get('password-repeat')

        user_email = Users.query.filter_by(email=email).first()
        user_username = Users.query.filter_by(username=username).first()

        if user_email:
            flash('Email Address already in use.', category='error')
        elif user_username:
            flash(f'Username `{user_username.username}` already in use.', category='error')
        elif not username or not email or not password or not repeat_pass:
            flash('All fields are required!', category='error')
        elif not re.match(r'^[a-zA-Z0-9._-]+$', username):
            flash("Invalid username! Usernames can only include letters, numbers, dots (.), dashes (-), " \
                  "and underscores (_). No special characters or spaces are allowed.", category='error')
        elif password != repeat_pass:
            flash("Passwords do not match!", category='error')
        else:
            new_user = Users(email=email, username=username, password=generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
            flash("Account Created!", category='success')
            login_user(new_user, remember=True)
            return redirect(url_for('views.home'))

    return render_template('register.html', user=current_user)

@auth.route('/login', methods=('GET', 'POST'))
def login():

    if current_user.is_authenticated:  # Check if the user is already logged in
        return redirect(url_for('views.home'))
    
    if request.method == 'POST':

        email = request.form.get('email')
        password = request.form.get('password')

        user = Users.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                flash('Successfully logged in!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect Email or Password!', category='error')
        else:
            flash('Incorrect Email or Password!', category='error')

    return render_template('login.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from .models import users

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        repeat_pass = request.form.get('password-repeat')

        user = users.query.filter_by(email=email).first()
        
        if user:
            flash('Email already exists.', category='error')
        elif not username or not email or not password or not repeat_pass:
            flash('All fileds required!', category='error')
        elif password != repeat_pass:
            return "Passwords do not match!", 400

    return render_template('register.html')

@auth.route('/login')
def login():
    return "login"

@auth.route('/logout')
def logout():
    return "logout"

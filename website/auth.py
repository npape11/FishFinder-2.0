from flask import Flask, Blueprint, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        repeat_pass = request.form.get('password-repeat')

        if not username or not email or not password or not repeat_pass:
            return "All fields are required!", 400

        if password != repeat_pass:
            return "Passwords do not match!", 400

        hashed_pass = generate_password_hash(password)

    return render_template('register.html')

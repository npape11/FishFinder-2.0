from flask import Flask, Blueprint, render_template, request, redirect, url_for

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "home"

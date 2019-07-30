from app.movies import main
from app import db
from app.movies.models import Movie
from flask import render_template, url_for, request

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/register')
def register():
    return render_template('register.html')

@main.route('/login')
def login():
    return render_template('login.html')

@main.errorhandler(404)
def page_not_found(e):
    return render_template('notfound.html')
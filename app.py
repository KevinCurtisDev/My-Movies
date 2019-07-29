from flask import Flask, render_template, request, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config.update(
    SECRET_KEY='K155MyA551981',
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:K155MyA551981@localhost/movies_db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

db = SQLAlchemy(app)

class Movie(db.Model):
    __tablename__ = 'movie'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False, index=True)
    director = db.Column(db.String(55))
    avg_rating = db.Column(db.Float)
    image = db.Column(db.String(100), unique=True)
    release_date = db.Column(db.String(10)) 

    def __init__(self, title, director, avg_rating, image, release_date):

        self.id = id
        self.title = title
        self.director = director
        self.avg_rating = avg_rating
        self.image = image
        self.release_date = release_date

    def __repr__(self):
        return '{} by {}'.format(self.title, self.director)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('notfound.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
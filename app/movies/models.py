from app import db

#Create a Movie table class
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
"""Models for movie ratings app."""
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user of movie ratings app"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        autoincrement = True,
                        nullable = False,
                        primary_key = True)

    email = db.Column(db.String, unique = True, nullable = False)

    password = db.Column(db.String, nullable = False)

     # ratings = a list of Rating objects

    def __repr__(self):
        return f"<User user_id = {self.user_id} email = {self.email}>"


class Movie(db.Model):
    """A movie in the movie rating app"""

    __tablename__ = "movies"

    movie_id = db.Column(db.Integer,
                         autoincrement = True,
                         primary_key = True)
    title = db.Column(db.String)
    overview = db.Column(db.Text)
    release_date = db.Column(db.DateTime) #Read up on DateTime for project
    poster_path = db.Column(db.String)

     # ratings = a list of Rating objects

    def __repr__(self):
        return f"<Moive movie_id = {self.movie_id}, title = {self.title}>"


class Rating(db.Model):
    """Rating for movies in movie rating app"""

    __tablename__ = "ratings"

    rating_id = db.Column(db.Integer,
                          autoincrement = True,
                          primary_key = True)
    score = db.Column(db.Integer)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.movie_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    movie = db.relationship('Movie', backref = 'ratings')
    user = db.relationship('User', backref = 'ratings')

    def __repr__(self):
        return f"<Rating rating_id = {self.rating_id} score = {self.score}>"


def connect_to_db(flask_app, db_uri='postgresql:///ratings', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)

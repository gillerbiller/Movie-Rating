"""Server for movie ratings app."""

from flask import (Flask, render_template, request, 
                   flash, session, redirect)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route("/")
def homepage():
    """Renders the hompage."""

    return render_template("homepage.html")

@app.route("/movies")
def all_moives():

    movies = crud.get_movies()

    return render_template("all_movies.html", movies = movies)

@app.route("/movies/<movie_id>")
def show_movie(movie_id):
    """Show details of a certain movie."""

    movie = crud.get_movie_by_id(movie_id)

    return render_template('movie_details.html', movie = movie)    

@app.route("/users")
def all_users():

    users = crud.get_users()

    return render_template("all_users.html", users = users)

@app.route("/users/<user_id>")
def user_profile(user_id):
    """Show profile of a certain user"""

    user = crud.get_user_by_id(user_id)

    return render_template('user_profile.html', user = user)

@app.route("/users", methods=['POST'])
def register_user():
    """Make a new user."""

    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)

    if user:
        flash("That email seems to already have an account linked to it. \
Please try again.")
    else:
        crud.create_user(email, password)
        flash("Account created!")
    return redirect('/')



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)

"""Server for holistic health directory app"""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db

import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """return homepage template"""

    return render_template('homepage.html')

@app.route('/signin')
def signin():
    """View login page"""

    return render_template('login.html')

@app.route('/add-user')
def add_user():
    """View add user page"""

    return render_template('register-form.html')

@app.route('/directory')
def all_businesses():
    """View all businesses"""
    user_id = session.get("user_id")
    flash(user_id)
    # bus_id = need to get bus
    all_bus = crud.get_businesses()

    return render_template('all_businesses.html', all_bus=all_bus)

@app.route('/directory/<bus_id>')
# TODO: potentially change this so its directory/bus_name through a different query (.filter or.filter_by)
def show_business(bus_id):
    """Show details on a particular business"""

    business = crud.get_bus_by_id(bus_id)

    return render_template('/business_details.html', business=business)

@app.route('/login', methods=['POST'])
def login_user():
    """Log a user into the website"""

    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.check_user_login_info(email, password)

    if user:
        session["user_id"] = user.user_id
        return redirect('/directory')

    else:
        flash('Login info is incorrect, try again.')
        return redirect('/signin')
    

@app.route('/user-registration', methods=['POST'])
def register_user():
    """add a user to the user table in the db"""

    fname = request.form.get('fname')
    lname = request.form.get('lname')
    email = request.form.get('email')
    password = request.form.get('password')
    tel = request.form.get('tel')

    user = crud.get_user_by_email(email)
    # Check to see if user exists in db already

    if user:
        flash('This email already exists. Log in or try again.')
        return redirect('/user-registration')
    else:
        user = crud.create_user(fname, lname, email, password, tel)

        # add the user to the session:
        # session["user_id"] = user.user_id
        flash('Account created sucessfully! Please log in')

        return render_template('login.html')

@app.route('/about')
def about_us():
    """return about us template"""

    return render_template('about_us.html')

@app.route('/events')
def all_evts():
    """View all events"""

    all_evts = crud.get_events()

    return render_template('all_evts.html', all_evts=all_evts)

@app.route('/profile')
def profile():
    """Show a user's profile"""
    user_id = session.get("user_id")

    if user_id:
        user = crud.get_user_by_id(user_id)
        return render_template('user_profile.html', user=user)
    
    else:
        flash('Please sign in')
        return render_templated('login.html')

@app.route('/user-favorites')
def show_faves():
    """show a list of a user's favorited businesses"""

    user_id = session.get("user_id")

    if user_id:
        user = crud.get_user_by_id(user_id)
        joined_faves = crud.get_bus_by_user_id(user_id)

        return render_template('favorites.html', user=user, joined_faves=joined_faves)
    
    else:
        flash('Please sign in')
        return render_templated('login.html')


    # query into users_buss by id, to get out the bus_id.all()
    # query to see all of the bus_id's connected with a single user_id
    # UserBus.bus_id.all()
    # user.bus_id.all()
    # take those bus_id's and show the name of the business and link to bus page




if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
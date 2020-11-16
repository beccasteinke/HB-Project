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
    user_id = session.get("user_id")
    if user_id:
        flash(user_id)

    return render_template('homepage.html')

@app.route('/signin')
def signin():
    """View login page"""
    user_id = session.get("user_id")
    if user_id:
        flash(user_id)

    return render_template('login.html')

@app.route('/add-user')
def add_user():
    """View add user page"""

    return render_template('register-form.html')

@app.route('/directory')
def all_businesses():
    """View all businesses"""
    # TODO: get rid of user flash
    user_id = session.get("user_id")
    if user_id:
        flash(user_id)
    # bus_id = need to get bus
    all_bus = crud.get_businesses()

    return render_template('all_businesses.html', all_bus=all_bus)

@app.route('/add-business')
def add_bus():
    """View add business page"""

    return render_template('bus-add-form.html')

# TODO: service isn't quite matching up. 
# Need to take the service input and turn it into a service id, so I can add it to the DB
@app.route('/business-registration', methods=['POST'])
def register_bus():
    """add a business to the business table in the db"""

    bus_name = request.form.get('bus_name')
    url = request.form.get('url')
    address = request.form.get('address')
    email = request.form.get('email')
    tel = request.form.get('tel')
    description = request.form.get('description')
    image = request.form.get('image')
    service = request.form.get('name_serv')
    bus_passwrd = request.form.get('bus_passwrd')

    bus = crud.get_bus_by_email(email)
    # Check to see if user exists in db already

    if bus:
        flash('This business already exists.')
        return redirect('/business-registration')
    else:
        if service == 'bodywork':
            service_id = 1
        elif service == 'breathwork':
            service_id = 2
        elif service == 'energy-work':
            service_id = 3
        elif service == 'fitness':
            service_id = 4
        elif service == 'halotherapy':
            service_id = 5
        elif service == 'meditation':
            service_id = 6
        elif service == 'mental-health':
            service_id = 7
        elif service == 'nutrition':
            service_id = 8
        elif service == 'sound-healing':
            service_id = 9
        elif service == 'yoga':
            service_id = 10
        else:
            service_id = 11

        bus = crud.add_new_business(bus_name, url, address, email, tel, description, image, service_id, bus_passwrd)

        flash('Your business has been added successfully!')

        return redirect('/directory')
    
@app.route('/business-signin')
def bus_login():
    """View business login page"""

    return render_template('business-login.html')

@app.route('/search')
def show_search():
    """View search page"""

    return render_template('search.html')

@app.route('/business-login', methods=['POST'])
def login_bus():
    """Log a business into the website"""

    email = request.form.get('email')
    bus_passwrd = request.form.get('bus_passwrd')

    business = crud.check_bus_login_info(email, bus_passwrd)

    if business:
        session["bus_id"] = business.bus_id
        return redirect('/directory')

    else:
        flash('Login info is incorrect, try again.')
        return redirect('/business-signin')

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


# TODO: make this do the thing its supposed to do
@app.route('/events/<bus_id>')
def show_bus_evts(bus_id):

    all_bus_evts = crud.get_evt_by_bus(bus_id)
    # add to UserBus

    return render_template('evts_by_bus.html', bus_id=bus_id)


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
        return render_template('login.html')

@app.route('/add-favorite/<bus_id>', methods=['POST', 'GET'])
def add_fave(bus_id):

#TODO: bus is being sucessfully added, JS is changing icon
# .... page is reloading so icon changes back
# Using crud function that is identical to the create userbus
# TODO: if already exists in db, do not re add

    user_id = session.get("user_id")

    user = crud.get_user_by_id(user_id)

    # bus_id = request.form.get(name)
    business = crud.get_bus_by_id(bus_id)

    if user:
        fave = crud.add_new_userbus(user, business)
        added_fave = crud.check_userbus_info(user_id, bus_id)

        if added_fave:
            flash("you've already added this to your favorites list")


    return redirect('/directory')




if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
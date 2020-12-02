"""Server for holistic health directory app"""

from flask import (Flask, render_template, request, flash, session, redirect, url_for, jsonify)
from model import connect_to_db, Business, Event
import random
from flask_uploads import (configure_uploads, IMAGES, UploadSet)
from werkzeug import secure_filename, FileStorage
from forms import SearchForm
from tables import BusResults, EvtResults

import crud
from jinja2 import StrictUndefined



import pickle









app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

# Configuring a default folder for uploaded images
app.config['UPLOADED_PHOTOS_DEST'] = 'static/jpeg'
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)


@app.route('/')
def homepage():
    """return homepage template"""

    # if 'user_id' in session:
    #     return render_template('homepage.html')

    return render_template('homepage.html')

@app.route('/googlecal')
def show_cal():

    return render_template('googleCal.html')

@app.route('/signin')
def signin():
    """View login page"""

    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_user():
    """Log a user into the website"""

    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.check_user_login_info(email, password)

    if user:
        session["user_id"] = user.user_id
        session['logged_in'] = True
        fname = user.fname
        flash(f'Welcome {fname}')
        return redirect('/directory')

    else:
        flash('Login info is incorrect, try again.')
        return redirect('/signin')

#TODO; FIX THIS ROUTE and lOGIN/LOGOUT SHIT
@app.route('/isloggedin')
def is_logged_in():
# TODO: authenticate 
    
    if session['logged_in']:
        return jsonify(session['logged_in'])
    else:
        return jsonify(False)

    # # if user_id exists in session - return != None

    # else:
    #     return jsonify(session["user_id"] == None)

@app.route('/logout')
def user_logout():
    """Log a user out"""

    session.pop('logged_in', None)
    flash('You are now logged out')

    return redirect('/')

@app.route('/add-user')
def add_user():
    """View add user page"""

    return render_template('register-form.html')

@app.route('/directory', methods=['GET', 'POST'])
def all_businesses():
    """View all businesses"""

    all_bus = crud.get_businesses()

    all_servs = crud.get_servs()

    # evts_bus = crud.get_evt_by_bus(bus_id)

    """Search form"""
    search = SearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)

    return render_template('all_businesses.html', all_bus=all_bus, all_servs=all_servs, form=search)

@app.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']

    if search_string:
        if search.data['select'] == 'Business':
            """if a user searches for a business"""
            qry = crud.db.session.query(Business).filter(
                Business.bus_name.contains(search_string))
            results = qry.all()
            table = BusResults(results)

        elif search.data['select'] == 'Event':
            """if a user searches an event"""
            qry = crud.db.session.query(Event).filter(
                Event.name_evt.contains(search_string))
            results = qry.all()
            table = EvtResults(results)
        else:
            qry = crud.db.session.query(Business)
            results = qry.all()
    else:
        qry = crud.db.session.query(Business)
        results = qry.all()

    # if search.data['search'] == '':
    #     qry = crud.db.session.query(Business)
    #     results = qry.all()
    
    if not results:
        flash('No results found')
        return redirect('/directory')
    else:
        #display results
        table.border = True

        return render_template('results.html', table=table)

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
    image = photos.save(request.files['photo'])
    # image_save = images.save(form.dog_img.data)
    service = request.form.get('name_serv')
    bus_passwrd = request.form.get('bus_passwrd')

    bus = crud.get_bus_by_email(email)

    # Check to see if bus exists in db already
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

@app.route('/calendar')
def show_calendar():
    """View calendar page"""

    return render_template('calendar.html')

@app.route('/business-login', methods=['POST'])
def login_bus():
    """Log a business into the website"""

    email = request.form.get('bus-email')
    bus_passwrd = request.form.get('bus-passwrd')

    business = crud.check_bus_login_info(email, bus_passwrd)

    if business:
        session["bus_id"] = business.bus_id
        return redirect('/directory')

    else:
        flash('Login info is incorrect, try again.')
        return redirect('/business-signin')

@app.route('/business-profile')
def show_bus_profile():
    """Show a business profile"""
    bus_id = session.get("bus_id")

    if bus_id:
        business = crud.get_bus_by_id(bus_id)
        return render_template('bus_profile.html', business=business)
    
    else:
        flash('Please sign in')
        return render_template('login.html')

@app.route('/directory/<bus_name>')
def show_business(bus_name):
    """Show details on a particular business"""
    print(bus_name)
    print("********* bus name up top")
    business = crud.get_bus_by_name(bus_name)
    print(business)
    print("************ business up top")

    return render_template('/business_details.html', business=business)

@app.route('/directory/service/<service_id>')

def serv_filter(service_id):
    """show all businesses that provide a name_serv"""

    businesses = crud.bus_by_serv(service_id)

    return render_template('/filtered_businesses.html', businesses=businesses)

@app.route('/events/<bus_id>')
# TODO: potentially change this so its directory/bus_name through a different query (.filter or.filter_by)
def show_evts(bus_id):
    """Show events being put on by a particular business"""

    events = crud.get_bus_evts(bus_id)
    business = crud.get_bus_by_id(bus_id)

    return render_template('/business_events.html', events=events, business=business)

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

#TODO: finish this route

# @app.route('/add-event', methods=['POST'])
# def add_event():
#     """add a new event to the business's profile and db"""

#     business = request.form.get('bus_name')
#     name_evt = request.form.get('name_evt')

#     start = request.form.get('start')
#     end = request.form.get('end')
#     description = request.form.get('description')

#     #TODO might run into service option problems
#     service = request.form.get('service')

#     #business = get bus_id from session?

#     new_evt = crud.create_event(name_evt, start, end, description, service, business)

#     return redirect('/')


@app.route('/profile')
def profile():
    """Show a user's profile"""

    user_id = session.get("user_id")
    userbuses = crud.show_all_userbus(user_id)

 

    if user_id:
        user = crud.get_user_by_id(user_id)
        return render_template('user_profile.html', user=user, userbuses=userbuses)
    
    else:
        flash('Please sign in')
        return render_template('login.html')

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
        # added_fave = crud.check_userbus_info(user_id, bus_id)

        # if added_fave:
        #     flash("you've already added this to your favorites list")


    return redirect('/directory')


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)









# google cal play
# from googleapiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request

# # users can read/write on the entire calendar
# # maybe change to https://www.googleapis.com/auth/calendar.events.readonly 
# # so users can just see the events in a calendar
# scopes = ['https://www.googleapis.com/auth/calendar']
# flow = InstalledAppFlow.from_client_secrets_file("client_secret2.json", scopes=scopes)
# credentials = flow.run_console()

# pickle.dump(credentials, open("token.pkl", "wb"))

# credentials = pickle.load(open("token.pkl", "rb"))

# service = build("calendar", "v3", credentials=credentials)

# calendars = service.calendarList().list().execute()

# calendar_id = calendars['items'][0]['id']

# # all events on OMH calendar
# result = service.events().list(calendarId=calendar_id).execute()

# print(result)
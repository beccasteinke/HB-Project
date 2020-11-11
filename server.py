"""Server for holistic health directory app"""

from flask import Flask, render_template, request, flash, session, redirect
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

@app.route('/about')
def about_us():
    """return about us template"""

    return render_template('about_us.html')

@app.route('/directory')
def all_businesses():
    """View all businesses"""

    all_bus = crud.get_businesses()
    # busservs = crud.get_busservs()

    return render_template('all_businesses.html', all_bus=all_bus)#, busservs=busservs)

# @app.route('/directory/<bus_name>')

@app.route('/events')
def all_evts():
    """View all events"""

    all_evts = crud.get_events()

    return render_template('all_evts.html', all_evts=all_evts)

@app.route('/profile')
def profile():
    """Show a user's profile"""

    return render_template('user_profile.html')

@app.route('/login', methods=['POST', 'GET'])
def user_login():
    """Log a user into the website"""

    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.check_user_login_info(email, password)
    print(user)

    # if "user_id" not in session:
    #     session["user_id"] = user.user_id
    # else:
    #     active_user = session.get("user_id")

    if user:
        flash("Successful login")
    else:
        flash("Login info incorrect, please try again")
    
    return redirect('/')

# @app.route('/login', methods=['POST', 'GET'])
# def register_user():
#     """Register a new user"""

#     email = request.form.get('email')
#     password = request.form.get('password')
#     fname = request.form.get('fname')
#     lname = request.form.get('lname')
#     tel = request.form.get('tel')

#     user = crud.get_user_by_email(email)
    
#     """Check to see if user is already in database"""
#     if user:
#         flash("This email already exists. Try again")
#     else:
#         crud.create_user(fname, lname, email, password, tel)
#         flash("Your account was created successfully")

#     return redirect('/')


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
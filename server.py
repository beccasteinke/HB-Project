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

@app.route('/login')
def login_user():
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)
    if user:
        return "This email is registered, you are logged in"
        # return 'A user already exists with that email.'
    else:
        # flash("This email is not registered. Create an account")
        return redirect('/')

@app.route('/register', methods=['POST', 'GET'])
def check_user():
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)
    if user:
        return "This email is registered, you are now logged in"
    else:
        def register_user():
            fname = request.form['fname']
            lname = request.form['lname']
            email = request.form['email']
            password = request.form['password']
            tel = request.form['tel']

    # if user:
    #     return "A user already exists with that email"
    # else:
    #     crud.create_user(fname, lname, email, password, tel)

    return render_template('register-form.html')
        # create_user(email, password)

        # return redirect('/login-form')

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
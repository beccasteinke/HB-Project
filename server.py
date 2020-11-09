"""Server for holistic health directory app"""

from flask import (Flask, render_template, request, flash, session, redirect)

app = Flask(__name__)

@app.route('/')
def homepage():
    """return homepage template"""

    return render_template('homepage.html')

# @app.route('/register', methods=['POST'])
# def register_user():
#     email = request.form['email']
#     password = request.form['password']

#     user = get_user_by_email(email)
#     if user:
#         return 'A user already exists with that email.'
#     else:
#         create_user(email, password)

#         return redirect('/login-form')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
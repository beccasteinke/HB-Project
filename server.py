"""Server for holistic health directory app"""

from flask import (Flask, render_template, request, flash, session, redirect)

app = Flask(__name__)

@app.route('/')
def homepage():
    """return homepage template"""

    return render_template('homepage.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
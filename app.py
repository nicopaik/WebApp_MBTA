"""
Amazing app to help you find nearest MBTA station
"""
from flask import Flask, request, render_template, redirect, url_for, session
from mbta_helper import find_stop_near

app = Flask(__name__)

# @app.route('/')
# def index():
#     """
#     displays index.html as homepage
#     """
#     return render_template('index.html')


@app.route('/', methods = ['POST', 'GET'])
def find_stop():
    """
    Upon clicking the 'Submit' button, the data from the form will be sent via a POST
    request to the Flask backend at the route POST /nearest
    """
    if request.method == 'POST':
        place_name = request.form['text']
        print(place_name)

        try:
            stop, message = find_stop_near(place_name)
            return render_template('results.html', station=stop, wheelchair_accessibility=message)
        except:
            return render_template('error.html')
    else:
        return render_template('form.html')

    
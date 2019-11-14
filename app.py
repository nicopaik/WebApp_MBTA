"""
Amazing app to help you find nearest MBTA station
"""
from flask import Flask
from mbta_helper import find_stop_near

app = Flask(__name__)

@app.route('/')
def index():
    """"
    displays index.html as homepage
    """"
    return "Index Page"

@app.route('/<place_name>')
def get_stop(place_name):
    stop, is_accessible =  find_stop_near(place_name)
    if stop:
        if is_accessible == 1:
            return f'{stop} is accessible to wheelchairs'
        else:
            return f'{stop} is not accesible to wheelchairs'

            

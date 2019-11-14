"""
Amazing app to help you find nearest MBTA station
"""

from flask import Flask
from mbta_helper import *


app = Flask(__name__)


@app.route('/')
def index():
    return "Index Page"

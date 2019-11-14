"""
Amazing app to help you find nearest MBTA station
"""

from flask import Flask, render_template
from mbta_helper import *


app = Flask(__name__)


@app.route('/')
def index():
    """
    display index as homepage
    """
    return render_template('index.html')

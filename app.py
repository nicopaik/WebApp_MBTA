"""
Amazing app to help you find nearest MBTA station
"""
from flask import Flask, render_template
from mbta_helper import find_stop_near

app = Flask(__name__)

@app.route('/')
def index():
    """
    displays index.html as homepage
    """
    return render_template('index.html')


@app.route('/nearest', methods = ['POST'])
def find_stop():
    """
    Upon clicking the 'Submit' button, the data from the form will be sent via a POST
    request to the Flask backend at the route POST /nearest
    """
    
    

@app.route('/nearest_mbta', methods=['GET', 'POST'])
def nearest_stop():
    '''
    The Flask backend will handle the request to POST /nearest_mbta.
    Then your app will render a mbta_station page for the user - presenting nearest MBTA stop
    and whether it is wheelchair accessible. In this step, you need to use the code from Part 1
    '''
    

import urllib.request
import json
from pprint import pprint

# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://open.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# Your API KEYS (you need to use your own keys - very long random characters)
MAPQUEST_API_KEY = L7NHzNvuOR9Gm0h12LJF6BBZ3855ha8D
MBTA_API_KEY = 82629ccee2ca4a40b1410cb8711a184b



# A little bit of scaffolding if you want to use it

def get_json(url):
    """
    Given a properly formatted URL for?agger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    url = f'http://www.mapquestapi.com/geocoding/v1/address?key={L7NHzNvuOR9Gm0h12LJF6BBZ3855ha8D}&location=Babson%20College'
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    pprint(response_data)


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    pass


def main():
    """
    You can all the functions here
    """
    pass


if __name__ == '__main__':
    main()

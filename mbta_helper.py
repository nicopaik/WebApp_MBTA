import urllib.request
import json
from pprint import pprint

# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://open.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# Your API KEYS (you need to use your own keys - very long random characters)
MAPQUEST_API_KEY = "L7NHzNvuOR9Gm0h12LJF6BBZ3855ha8D"
MBTA_API_KEY = "6527b5fff8394156b8877887d9db2a65"



# A little bit of scaffolding if you want to use it

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    # url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Babson%20College'
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    return response_data
    # pprint(response_data)

def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding  API URL formatting requirements.
    """
    place_name = place_name.replace(' ', '%20')
    url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={place_name}'
    response_data = get_json(url)
    response_data1 = response_data["results"][0]["locations"][0]['latLng']
    latitude = response_data1['lat']
    longitude = response_data1['lng']
    return latitude, longitude


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    url = f'{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance'
    response_data = get_json(url)
    station =  response_data['data'][0]['attributes']['name']
    wheelchair = response_data['data'][0]['attributes']['wheelchair_boarding']
    if wheelchair == 0:
        message = 'No information whether this station is wheelchair accessible.'
    elif wheelchair == 1:
        message = 'This station is wheelchair accessible.'
    else:
        message = 'This station is wheelchair inaccessible.'
    return station, message


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    lat, lng = get_lat_long(place_name)
    # return lat, lng
    return get_nearest_station(lat, lng)


def main():
    """
    You can have all the functions here
    """
    # print(get_json(MAPQUEST_API_KEY))
    # place_name = 'Prudential Center'
    # print(f'The latitude and longitude of {place_name} is:')
    # print(get_lat_long(place_name))

    # print(f'The nearest MBTA station to {place_name} is:')
    # print(get_nearest_station(42.3489,-71.08182))

    # print(f'The nearest MBTA station to Northeastern University is:')
    # print(find_stop_near('Mortheastern University'))

    print(find_stop_near('prudential center'))


if __name__ == '__main__':
    main()
import requests
import json
from BaseGeocoder import BaseGeocoder
from BaseGeocoder import Geolocation

class GeonamesGeocoder(BaseGeocoder):
    """encapsulates Geonames.com geocoder web service"""
    
    def __init__(self, key): 
        self.key = key
        self.GEOCODER_ID = "Geonames"
        self.SERVICE_URI = "http://api.geonames.org/geocodeJSON?"
        self.KEY_PARAM_NAME = "username"
        self.ADDRESS_PARAM_NAME = "q"

    def query_service(self, address):  
        response = requests.get(self.serviceURI(address))

        print("google queried with:" + address)
        print(str(response))
        
        if response.status_code != requests.codes.ok:
            response.raise_for_status() 

        print(response.text)

        responseJSON = json.loads(response.text)

        
        latitude = responseJSON['geoCoderResult']['lat']
        longitude = responseJSON['geoCoderResult']['lng']
        requested_geocode = Geolocation(latitude, longitude)
        
        if requested_geocode.latitude is None or  requested_geocode.longitude is None:
            raise ValueError('expected json data from service missing')

        return requested_geocode
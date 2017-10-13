from BaseGeocoder import BaseGeocoder
from BaseGeocoder import Geolocation
import requests
import json


class GoogleGeocoder(BaseGeocoder):
    """encapsulates Geonames.com geocoder web service"""
     
    def __init__(self, key): 
        self.key = key
        self.GEOCODER_ID = "Google"
        self.SERVICE_URI = "https://maps.googleapis.com/maps/api/geocode/json?"
        self.KEY_PARAM_NAME = "key"
        self.ADDRESS_PARAM_NAME = "address"

    def query_service(self, address):  
        response = requests.get(self.serviceURI(address))

        print("google queried with:" + address)
        print(str(response))
        
        if response.status_code != requests.codes.ok:
            response.raise_for_status() 

        print(response.text)

        responseJSON = json.loads(response.text)

        
        latitude = responseJSON['results']['address_components']['geometry']['location']['lat']
        longitude = responseJSON['results']['address_components']['geometry']['location']['lng']
        requested_geocode = Geolocation(latitude, longitude)
        
        if requested_geocode.latitude is None or  requested_geocode.longitude is None:
            raise ValueError('expected json data from service missing')

        return requested_geocode



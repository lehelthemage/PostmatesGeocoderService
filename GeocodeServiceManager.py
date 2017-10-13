from BaseGeocoder import BaseGeocoder
from  GeonamesGeocoder import GeonamesGeocoder
from GoogleGeocoder import GoogleGeocoder


class GeocodeServiceManager(object):
    """encapsulates functionality of main geocoding service"""
    
    def __init__(self):
        self.geocoders = []


    #adds a geocoder service object to the list of geocoders in the manager
    #errors if trying to add a geocoder service of a certain type that is already in the list
    def add_geocoder_service(self, geocoder):
        if not isinstance(geocoder, BaseGeocoder):
            raise TypeError("geocoder object supplied was not a BaseGeocoder subclass")

        #check if geocoder's id matches any geocoder ids in the list
        for g in self.geocoders:
            if g.GEOCODER_ID == geocoder.GEOCODER_ID:
                raise RuntimeError("attempted to add duplicate geocoder service to manager")

        self.geocoders.append(geocoder)
        #return number of geocoders added
        return len(self.geocoders)


    #queries each geoder service in geocoder list stopping when valid geocode is returned
    def query_external_services(self, address):
        
        if len(self.geocoders) == 0:
            raise RuntimeError("attempted to query geocoding services without any geocoders registered")

        if address is None or not isinstance(address, str):
            raise ValueError('input address if not a valid string')

        num_failed_services = 0

        # try each geocoder service loaded until one works
        for geocoder in self.geocoders:
            try:
                geocoded_reponse = geocoder.query_service(address)
                print(geocoded_reponse)
            except:
                num_failed_services += 1


        if num_failed_services == len(self.geocoders):
            raise Exception("main and backup geocoding services failed to return geocodes")

        return geocoded_reponse







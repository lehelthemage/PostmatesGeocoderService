import mock
import unittest
from unittest.mock import patch 
from GeocodeServiceManager import GeocodeServiceManager
from  GoogleGeocoder import GoogleGeocoder
from  GeonamesGeocoder import GeonamesGeocoder
from  BaseGeocoder import BaseGeocoder
from BaseGeocoder import Geolocation

class MockGeocoder(BaseGeocoder):
    def __init__(self, key='', ret_lat=0, ret_lng=0): 
        self.returned_geocode = Geolocation(ret_lat,ret_lng)
    
        
    def query_service(self, address):
        return self.returned_geocode

class GeocodeServiceManagerTest(unittest.TestCase):
    """service manager tester"""


    def test_add_geocoder_service(self):
        service_manager = GeocodeServiceManager()
        
        #assert the geocoders list is empty
        self.assertEquals(len(service_manager.geocoders), 0)

        #test with adding garbage
        error_raised = False
        try:
            count = service_manager.add_geocoder_service(111)
        except:
            error_raised = True

        self.assertEquals(error_raised, True)

        #add a Google Geocoder to the manager and have it return 1
        geocoder = GoogleGeocoder("fake_key")
        count = service_manager.add_geocoder_service(geocoder)

        self.assertEquals(count, 1)

        #attempt to add a second Google geocoder to manager...
        error_raised = False
        try:
            service_manager.add_geocoder_service(geocoder)
        except:
            error_raised = True

        self.assertEquals(error_raised, True)


    def test_query_external_services(self):

        service_manager = GeocodeServiceManager()

        #add mock geocoder service object to manager
        count = service_manager.add_geocoder_service(MockGeocoder("123", 1, 2))

        self.assertEquals(count, 1)


        #call query_external_services
        geocode = service_manager.query_external_services("123 ABC St. Los Angeles, CA")
        self.assertEquals(geocode.latitude, 1)
        self.assertEquals(geocode.longitude, 2)


if __name__ == '__main__':
    unittest.main()


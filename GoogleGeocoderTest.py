import mock
import unittest
from unittest.mock import patch
from GoogleGeocoder import GoogleGeocoder
from BaseGeocoder import Geolocation


class GoogleGeocoderTest(unittest.TestCase):
    """description of class"""


    @patch('GoogleGeocoder.requests.get')
    def test_query_service(self, mock_get):
        
        geocoder = GoogleGeocoder("test")
        

         #test valid address
        mock_response = mock.Mock()
        mock_response.status_code = 200
        mock_response.content = '{"results":{"address_components":{"geometry":{"location":{"lat":"-100.0", "lng":"-89.0"}}}}'
        mock_get.return_value = mock_response
        geolocation = geocoder.query_service("123 Sesame St Los Angeles CA")

        self.assertEquals(geolocation.latitude, -100)
        self.assertEquals(geolocation.longitude, -89)


        #test with number for address
        response = None
        try:
            resposne = geocoder.query_service(12345)
        except ValueError:
            pass

        self.assertEquals(response, None)

        #test with None for address
        try:
            resposne = geocoder.query_service(None)
        except ValueError:
            pass

        self.assertEquals(response, None)
    

        
if __name__ == '__main__':
    unittest.main()
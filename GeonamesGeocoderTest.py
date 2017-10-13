import mock
import unittest
from unittest.mock import patch
from  GeonamesGeocoder import GeonamesGeocoder
from BaseGeocoder import Geolocation


class GeonamesGeocoderTest(unittest.TestCase):
    """geonames geocoder class unit tester"""

    @patch('GeonamesGeocoder.requests.get')
    def test_query_service(self, mock_get):
        
        geocoder = GeonamesGeocoder("test")
        

        #test valid address
        mock_response = mock.Mock()
        mock_response.status_code = 200
        mock_response.content = '{"geoCoderResult":{"lng":"-89.0","lat":"-100"}}'
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
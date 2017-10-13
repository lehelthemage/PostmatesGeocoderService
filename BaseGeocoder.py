from abc import ABC, abstractmethod;
import re 



class Geolocation(object):
    def __init__(self, lat=0, lng=0):
        if lat is None or lng is None:
            raise ValueError("Geolocation constructor cannot take params of None")
        self._latitude = float(lat);
        self._longitude = float(lng);

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude

    @latitude.setter
    def latitude(self, value):
        try:
            self._latitude = float(value)
        except ValueError:
            raise ValueError("assigning non-numeric value to geocode coordinate")

    @longitude.setter
    def longitude(self, value):
        try:
            self._longitude = float(value)
        except ValueError:
            raise ValueError("assigning non-numeric value to geocode coordinate")



class BaseGeocoder(ABC):
    """abstract base geocoder class"""

    @abstractmethod
    def __init__(self, key):
       pass
   
    @abstractmethod
    def query_service(self, address):
       pass

    def serviceURI(self, address):
       if address is None or not isinstance(address, str) or len(address) < 5:
           raise ValueError("address is not a valid string")
       if int(address[0]) == None:
           raise ValueError("address does not start with a numeral")
       #check if valid character are within
       print('adress before:' + address)
       if re.match("^[a-zA-Z0-9-.,\s]*$",address) is None:
           raise ValueError("illegal characters contained in address string")

       #replace white spaces with + character
       address.replace(' ', '+')

       uri = self.SERVICE_URI + self.KEY_PARAM_NAME + "=" + self.key + "&" + self.ADDRESS_PARAM_NAME + "=" + address
       print(uri)
       return uri
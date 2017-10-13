"""
This script runs the geocoder_service application using a development server.
"""
import os
import sys
from os import environ
from flask_api import FlaskAPI
from flask import request, jsonify, abort
from GeocodeServiceManager import GeocodeServiceManager
from GeonamesGeocoder import GeonamesGeocoder
from GoogleGeocoder import GoogleGeocoder

app = FlaskAPI(__name__, instance_relative_config=True)

@app.route('/geoservice/', methods=['GET'])
def geoservice():
    
    address = request.args.get('address') 
    service_manager = GeocodeServiceManager()
    service_manager.add_geocoder_service(GeonamesGeocoder("bardlehel"))
    service_manager.add_geocoder_service(GoogleGeocoder("AIzaSyBLJoZqzgcQJlULTKB36ahJYn-kBuq1eRE"))

    try:
        geocode = service_manager.query_external_services(address)
    except:
        response = jsonify(message="no gecoding services succeeded: " + str(sys.exc_info()))
        response.status_code = 400
        return response

    response = jsonify(input_address=address, latitude=geocode.latitude, longitude=geocode.longitude)
    response.status_code = 200
    return response

config_name = os.getenv('APP_SETTINGS') 

if __name__ == '__main__':
    app.run(debug=True)
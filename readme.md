**Title**
----
  Postmates Coding Challenge for Lehel Kovach (10/2017): Address Geocoder Web Service (RESTful) implemented in Python

  Queries third-party geocoding services (Geonames and Google currently), trying Geonames first and if no repsonse from that
  host, then falls back to Google's  service.

  This Web Service was implemented using the Flask-API module for Python.
  Developed and tested in Python 3.6 (64-bit) env

 * **Installation and Running**

 1) git clone this project to a new directory
 2) prepare a python 3.6 environment
 3) install required modules listed in requirements.txt
 4) in the shell, within the said environment, run: python GeocoderService/runserver.py

* **URL**

 /geoservice/?

* **Method:**
  
  GET
  
*  **URL Params**

		**Required:**

		address=[string]  
		
			****string must be white spaced city address starting with a street number
				and be at least 5 characters long.  Only alphanumeric characters as well as the following chars
				are allowed:  `.` `,` `-` white-spaces and `+` (+ can substitute for white spaces)

* **Success Response:**
  
  * **Code:** 200 
    **Content:**	`{"input_address": "1635 Post Ave Torrance", 
						"latitude": 33.832244, 
						"longitude": -118.32144
					}`
 
* **Error Response:**

  * **Code:** 400
    **Content:** `{ message : "geocoder services unreachable" }`


* **Sample Call:**

	curl http://localhost:5000/geoservice/?address=1635+Post+Ave+Torrance
  
* **Notes:**

  Version 0.1
  
  Unit tests may not cover enough edge-cases
  No integration testing, just mocks used

  The code is configurable so that a developer can easily add other third-party geocoder services to this Web Service
  by subclassing the BaseGeocoder class and then instantiating a new geocoder object from that class, passing in the required
  API key, followed by adding the geocoder to the ServiceManager object.


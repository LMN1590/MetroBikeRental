* Running this project:
    - Running the backend:
	+ Install all the required modules, listed below
	+ At the top-level folder, run the following command to set up the server to receive requets
	    "uvicorn main:app --reload --port 8000"
    - Running the frontend:
	+ Change the working directory to sub-folder UI-Bike
	    "cd .\UI-Bike\"
	+ Install Nodejs and npm.
	+ Install all the necessary components of the frontend
	    "npm install"
	+ Run the website
	    "npm run dev"
	+ Access the GUI through the following URL - port can be changed in the package.json file, in the scripts part:
	    "http://localhost:3006/"


* Modules used in the project:
    - Python Backend 
	1. Installed Requirements:
    	    + Python 3.8.5 (CPython)
            + sklearn-1.2.2: To import the NearestNeighbor model to be used in the project.
	    + numpy-1.24.3: One of the requirements of sklearn
	    + pandas-2.0.2: To get data into a Dataframe to be analyzed
	    + requests: To make HTTP request to the Metro bike endpoints to receive JSON data in the form of string
	    + json: To turn JSON data in the form of string into dictionaries that can be used in Python
	    + datetime: To get the date and time of update to the cache, to determine validity of data.
	    + sys: To be able to import module from different python files in different folders. 
	    + fastapi - 0.95.2: To create an API interface that can communicate with the frontend.
	    + uvicorn - 0.22.0: To run the API interface created by fastapi, receive and pass requests to the server.

        2. API:
	    + Bikeshare API:
		To receive data on the stations at downtown Los Angeles.
		URL: "https://bikeshare.metro.net/stations/json/"
	    + TravelTime API:
		To receive the time it takes to get to locations and the route to get there.
		URL: "https://api.traveltimeapp.com/v4/time-filter"

	3. Setting up the backend:
	    Using the top-level folder as current working directory, please run the following command:
		"uvicorn main:app --reload --port 8000"
	    This will create a server on your localhost, port 8000 that will receive requests based on the URL.	
	
	4. Making requests:
	    The server will receive two types of requests:
		a. Find requests:
		    Endpoint: "http://127.0.0.1:8000/find/"
		    Function: To find the k nearest stations that either have docks to return bikes or have bikes available to rent.
		    Parameters:
			* lat: Latitude of the starting location.
			* long: Longitude of the starting location
			* k: the number of stations to find
			* slots: the number of bikes or docks required to have 
			* reqType: the type of requests
		    Sample URL: "http://127.0.0.1:8000/find/?reqType=1&lat=34.035758&long=-118.266344&k=2&slots=1"
		    Result:
			* status: whether the request was successful
			* data: list of k nearest stations that satisfy the number of bikes or docks, based on request type.
			* type: the type of response
			* start: starting location.
		b. Route requests:
		    Endpoint: "http://127.0.0.1:8000/route/"
		    Function: To find easiest route from starting location to destination
		    Parameters:
			* startLat: Latitude of the starting location.
			* startLong: Longitude of the starting location
			* endLat: Latitude of the destination.
			* endLong: Longitude of the destination. 
			* slots: the number of bikes or docks required to have 
		    Sample URL: "http://127.0.0.1:8000/route/?startLat=34&startLong=-118&endLat=34.2&endLong=-118.5&slots=1"
		    Result:
			* status: whether the request was successful
			* data > startLoc: starting location
			* data > endLoc: destination
			* data > startStation: starting station to rent bikes, contain route from start location to station
			* data > endStation: ending station to return bikes, contain route from station to end location
			* data > routing: the route between the two station.
			* type: the type of response

    - React front-end:
	1. Installed Requirements:
	    + Nodejs - 18.14.0
	    + npm - 9.5.0
	    + vite
	    + jquery: to make API request to backend
	    + react, react-dom: framework to render webpage with more flexibility

	2. API:
	    + HereMap SDK:
		To display the Los Angeles map and markers, representing stations.

	3. Setting up the frontend:
	    Change the current working directory to the UI-Bike folder:
		"cd .\UI-Bike\"
	    Install all the necessary components using the following command:
		"npm install"
	    Run the frontend with the following command:
		"npm run dev"
	    Access the GUI through the following URL - port can be changed in the package.json file, in the scripts part:
		"http://localhost:3006/"
	
import requests
from datetime import datetime
import json

class TravelTimeProcess:
    _travel_time = 14400

    @staticmethod
    def getTimeDep(req, stationRes):
        stationList = stationRes['data']

        url = 'https://api.traveltimeapp.com/v4/time-filter'
        header = {
            'Content-Type': 'application/json',
            'X-Application-Id': '692368b0',
            'X-Api-Key': '2c80b96989135ed595d6225e9789cca5'
        }

        data = {}
        data['locations'] = TravelTimeProcess.generateLocationList(req,stationList)
        data['departure_searches'] = TravelTimeProcess.generateDepartSearch(stationList)

        raw = requests.post(url, headers=header, json = data).text
        raw = json.loads(raw)['results'][0]

        locations = raw['locations']
        unreachable = raw ['unreachable']

        TravelTimeProcess.processUnreachable(unreachable,stationList,'departure')
        TravelTimeProcess.processLocations(locations,stationList,'departure')

    @staticmethod
    def getTimeArrival(req, stationRes):
        stationList = stationRes['data']

        url = 'https://api.traveltimeapp.com/v4/time-filter'
        header = {
            'Content-Type': 'application/json',
            'X-Application-Id': '692368b0',
            'X-Api-Key': '2c80b96989135ed595d6225e9789cca5'
        }

        data = {}
        data['locations'] = TravelTimeProcess.generateLocationList(req,stationList)
        data['arrival_searches'] = TravelTimeProcess.generateArriveSearch(stationList)

        raw = requests.post(url, headers=header, json = data).text
        print(raw)
        raw = json.loads(raw)['results'][0]

        locations = raw['locations']
        unreachable = raw ['unreachable']

        TravelTimeProcess.processUnreachable(unreachable,stationList,'arrival')
        TravelTimeProcess.processLocations(locations,stationList,'arrival')

    ############################################################################################################

    @staticmethod
    def generateDepartSearch(stationList):
        search = {
            'id': "Departure search",
            "arrival_location_ids": [
                str(id)
                for id, station in enumerate(stationList)
            ],
            'departure_location_id': 'point',
            'departure_time': datetime.now().isoformat(),
            "travel_time": TravelTimeProcess._travel_time,
            'properties': [
                'travel_time',
                'route'
            ],
            'transportation': {
                "type": "walking"
            }
        }

        return [search]
    
    @staticmethod
    def generateArriveSearch(stationList):
        search = {
            'id': "Arrival search",
            "departure_location_ids": [
                str(id)
                for id, station in enumerate(stationList)
            ],
            'arrival_location_id': 'point',
            'arrival_time': datetime.now().isoformat(),
            "travel_time": TravelTimeProcess._travel_time,
            'properties': [
                'travel_time',
                'route'
            ],
            'transportation': {
                "type": "walking"
            }
        }

        return [search]
    


    ############################################################################################################

    @staticmethod
    def generateLocationList(req, stationList):
        locations = [{
            'id': str(id),
            "coords":{
                'lat': station.coords['lat'],
                'lng': station.coords['long']
            }
        } for id, station in enumerate(stationList)]
        locations.append({
            'id': 'point',
            "coords":{
                'lat': req.coords['lat'],
                'lng': req.coords['long']
            }
        })
        
        return locations

    ############################################################################################################

    @staticmethod
    def processUnreachable(unreachableList,stationList,type):
        for id in unreachableList:
            index = int(id)
            stationList[index].setTime(TravelTimeProcess._travel_time + 1)
            stationList[index].setRoute({})
            stationList[index].setRouteType(type)
    @staticmethod
    def processLocations(locations,stationList,type):
        for location in locations:
            index = int(location['id'])
            props = location['properties'][0]
            stationList[index].setTime(props['travel_time'])
            stationList[index].setRoute(props['route'])
            stationList[index].setRouteType(type)

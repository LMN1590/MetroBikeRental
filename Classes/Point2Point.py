import requests
import json
from datetime import datetime

class Point2Point:
    _travel_time = 14400
    @staticmethod
    def findRoute(startLoc,endLoc):
        startID = 'start'
        endID = 'end'
        url = 'https://api.traveltimeapp.com/v4/time-filter'
        header = {
            'Content-Type': 'application/json',
            'X-Application-Id': 'adc8b30b',
            'X-Api-Key': '6e9546feedbcd404834cc668f976348d'
        }

        data = {}
        data['locations'] = [
            Point2Point.createLocs(startLoc,startID),
            Point2Point.createLocs(endLoc,endID)
        ]
        data['departure_searches'] = [
            Point2Point.createRequest(startID,endID)
        ]

        raw = requests.post(url, headers=header, json = data).text
        raw = json.loads(raw)['results'][0]
        print(raw)
        unreachable = raw['unreachable']
        if(unreachable == []):
            props = raw['locations'][0]['properties'][0]
            return {
                'status': True,
                'data': {
                    "time": props['travel_time'],
                    "route": props['route']
                }
            }
        else:
            return{
                'status': False,
                'data':"Can't find the way :("
            }


    @staticmethod
    def createLocs(loc,id):
        return {
            "id": id,
            "coords": {
                "lat": loc.coords['lat'],
                'lng': loc.coords['long']
            }
        }
    
    @staticmethod
    def createRequest(startID,endID):
        search = {
            'id': "Departure search",
            "arrival_location_ids": [
                endID
            ],
            'departure_location_id': startID,
            'departure_time': datetime.now().isoformat(),
            "travel_time": Point2Point._travel_time,
            'properties': [
                'travel_time',
                'route'
            ],
            'transportation': {
                "type": "cycling"
            }
        }

        return search
    
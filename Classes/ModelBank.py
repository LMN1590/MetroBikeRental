from Model import Model
from Point2Point import Point2Point
class ModelBank:
    #modelsList

    #predict
    def __init__(self) -> None:
        self.modelsList={
            "renting": Model("renting"),
            "docking": Model("docking")
        }
    
    def predict(self,req):
        type = req.reqType
        if(type == 'renting' or type == 'docking'):
            res = self.modelsList[type].processReq(req)

        elif(type == 'routing'):
            res = self.routing(req)

        res['type'] = type
        return res
    
    def routing(self,routeReq):
        startLoc, endLoc = routeReq.locations.values()

        startStation = self.modelsList[startLoc.reqType].processReq(startLoc)
        endStation = self.modelsList[endLoc.reqType].processReq(endLoc, arrivalBool=True)
        if(startStation['status'] and endStation['status'] and not compareLoc(startStation['data'][0],endStation['data'][0])):
            startStation = startStation['data'][0]
            endStation = endStation['data'][0]
            return {
                "status": True,
                "data":{
                    'startLoc': startLoc,
                    'startStation': startStation,
                    'routing': Point2Point.findRoute(startStation, endStation),
                    'endStation': endStation,
                    'endLoc': endLoc
                }
            }
        else:
            return {
                "status": False,
                "data": {
                    'startLoc': startLoc,
                    'routing': Point2Point.findRoute(startLoc, endLoc),
                    'endLoc': endLoc
                }
            }

def compareLoc(start,end):
    return start.coords['lat'] == end.coords['lat'] and start.coords['long'] == end.coords['long']
from Model import Model

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

        return res
    
    def routing(self,routeReq):
        startLoc, endLoc = routeReq.locations.values()

        startStation = self.modelsList[startLoc.reqType].processReq(startLoc)
        endStation = self.modelsList[endLoc.reqType].processReq(endLoc)
        if(startStation['status'] and endStation['status'] and not compareLoc(startStation['data'][0],endStation['data'][0])):
            return {
                "status": True,
                "data":{
                    'startLoc': startLoc,
                    'startStation': startStation['data'][0],
                    'endStation': endStation['data'][0],
                    'endLoc': endLoc
                }
            }
        else:
            return {
                "status": False,
                "data": {
                    'startLoc': startLoc,
                    'endLoc': endLoc
                }
            }

def compareLoc(start,end):
    return start.coords['lat'] == end.coords['lat'] and start.coords['long'] == end.coords['long']
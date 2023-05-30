from Model import Model

class ModelBank:
    #modelsList

    #predict
    def __init__(self) -> None:
        self.modelsList={
            "renting": Model("renting", lambda station:station.utilAvailable['bikesAvailable'] > 0),
            "docking": Model("docking", lambda station:station.utilAvailable['docksAvailable'] > 0)
        }
    
    def predict(self,req):
        type = req.reqType
        if(type == 'renting' or type == 'docking'):
            res = self.modelsList[type].processReq(req,10)

        elif(type == 'routing'):
            res = self.routing(req)

        return res
    
    def routing(self,routeReq):
        startLoc, endLoc = routeReq.locations.values()

        startStation = self.modelsList[startLoc.reqType].processReq(startLoc)
        endStation = self.modelsList[endLoc.reqType].processReq(endLoc)

        return {
            'startLoc': startLoc,
            'startStation': startStation[0],
            'endStation': endStation[0],
            'endLoc': endLoc
        }
        
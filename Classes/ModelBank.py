from Model import Model
from Request import Request

def rentingFilter(station):
    return station.utilAvailable['bikesAvailable'] > 0

def dockingFilter(station):
    return station.utilAvailable['docksAvailable'] > 0

class ModelBank:
    #modelsList

    #predict
    def __init__(self) -> None:
        self.modelsList={
            "renting": Model("renting", rentingFilter),
            "docking": Model("docking", dockingFilter)
        }
    
    def predict(self,req):
        type = req.reqType
        if(type == 'renting' or type == 'docking'):
            res = self.modelsList[type].processReq(req,10)
            return res
        
import copy
import numpy as np
from sklearn.neighbors import NearestNeighbors

from BikeDataCache import BikeDataCache

class Model:
    stationsRaw = BikeDataCache(300,True)
    _modelsList = []
    #validity
    #validStations
    @staticmethod
    def dataCheckValid():
        if(not Model.stationsRaw.checkValid()):
            Model.stationsRaw.getNewData()
            for model in Model._modelsList:
                model.validity=False



    #checkValid
    #retrainModel
    #update
    #predict
    def __init__(self,reqType) -> None:
        self.reqType = reqType

        self.lastSlot=-1
        self.validity = False
        self.validStations = []
        self.NNmodel = NearestNeighbors(n_neighbors=2)
        Model._modelsList.append(self)


    def processReq(self,req):
        Model.dataCheckValid()
        
        if(self.validity==False or self.lastSlot!=req.slots):
            self.filterData(req.slots)
            self.retrain()
            self.lastSlot = req.slots
            self.validity=True
        
        res = self.predict(req)
        return res


    def filterData(self, slots):
        self.validStations = list(filter(filterWrapper(self.reqType,slots), Model.stationsRaw.stations))

    def retrain(self):
        stationsCoords = [[station.coords['lat'], station.coords['long']] for station in self.validStations]
        if(len(self.validStations) > 0):
            self.NNmodel.fit(stationsCoords)

    def predict(self,req):
        reqCoords = [[req.coords['lat'], req.coords['long']]]
        if(len(self.validStations) > req.k):
            stationResult = self.NNmodel.kneighbors(reqCoords,n_neighbors=req.k)[1].tolist()[0]
            return {
                "status": True,
                "data": [self.validStations[index] for index in stationResult]
            }
        else:
            return {
                "status": False,
                "data": "No Valid Slots"
            }

def filterWrapper(reqType, slots):
    if reqType == 'renting':
        criteria = 'bikesAvailable'
    elif reqType == 'docking':
        criteria = 'docksAvailable'
    return lambda station:station.utilAvailable[criteria] >= slots

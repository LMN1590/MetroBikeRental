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
    def __init__(self,reqType,filterMethod) -> None:
        self.reqType = reqType
        self.filterMethod = filterMethod

        self.validity = False
        self.validStations = []
        self.NNmodel = NearestNeighbors(n_neighbors=2)
        Model._modelsList.append(self)


    def processReq(self,req,k=1):
        Model.dataCheckValid()
        
        if(self.validity==False):
            self.filterData()
            self.retrain()
            self.validity=True
        
        res = self.predict(req,k)
        return res


    def filterData(self):
        self.validStations = list(filter(self.filterMethod, Model.stationsRaw.stations))

    def retrain(self):
        stationsCoords = [[station.coords['lat'], station.coords['long']] for station in self.validStations]
        self.NNmodel.fit(stationsCoords)

    def predict(self,req,k):
        reqCoords = [[req.coords['lat'], req.coords['long']]]
        stationResult = self.NNmodel.kneighbors(reqCoords,n_neighbors=k)[1].tolist()[0]
        print([{
            'name': self.validStations[index].name,
            'util': self.validStations[index].utilAvailable,
            'coords': self.validStations[index].coords
        } for index in stationResult])

        return [self.validStations[index] for index in stationResult]

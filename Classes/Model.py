import copy
import numpy as np
from sklearn.neighbors import NearestNeighbors

from BikeDataCache import BikeDataCache

class Model:
    stationsRaw = BikeDataCache(10)
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


    def processReq(self,req,k):
        Model.dataCheckValid()
        
        if(self.validity==False):
            self.filterData()
            self.retrain()
            self.validity=True
        
        res = self.predict(req,k)
        return res


    def filterData(self):
        self.validStations = list(filter(Model.stationsRaw.stations, self.filterMethod))

    def retrain(self):
        self.NNmodel.fit([[station['coords']['lat'], station['coords']['long']] for station in self.validStations])

    def predict(self,req,k):
        self.NNmodel.kneighbors([req['coords']['lat'], req['coords']['long']],n_neighbors=k)

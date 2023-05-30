import json
import datetime
import requests

from Stations import Stations

class BikeDataCache:
    def __init__(self, timeLimit, testBool = False, url = "https://bikeshare.metro.net/stations/json/") -> None:
        self.timeLimit=timeLimit
        self.testBool=testBool
        self.url=url
        self.time=datetime.datetime.today()

        dictStations=self.getData()   
        self.stations=self.createStationsList(dictStations)
    
    def getData(self):
        if(self.testBool):
            return self.getDataLocal()
        else:
            return self.getDataOnline()
    def getDataLocal(self):
        file = open('./Sample/data.json')
        return json.load(file)
    def getDataOnline(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}
        getResult = requests.get(self.url, headers=headers).text
        return json.loads(getResult)
    
    def createStationsList(self,dictStations):
        return [Stations(raw) for raw in dictStations['features']]




    def checkValid(self):
        curTime = datetime.datetime.today()
        
        diffTime = (curTime-self.time).total_seconds()
        return diffTime < self.timeLimit
            
    def getNewData(self):
        dictStations = self.getData()
        self.stations=self.createStationsList(dictStations)

        self.time = datetime.datetime.today()


    

    def debug(self):
        print(self.timeLimit)
        print(self.time)
        for station in self.stations[:5]:
            station.debug()
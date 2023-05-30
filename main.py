from typing import Union
from fastapi import FastAPI

import sys
sys.path.insert(1, './Classes')
sys.path.insert(2, './Global')

from reqType import requestType
from ModelBank import ModelBank
from Request import Request
from RoutingReq import RoutingRequest

app = FastAPI()
app.bank = ModelBank()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/route/")
async def routing(startLat:float, startLong:float, endLat:float, endLong:float):
    startLoc = {
        'lat': startLat,
        'long': startLong
    }

    endLoc = {
        'lat': endLat,
        'long': endLong
    }
    
    req = RoutingRequest(startLoc,endLoc)
    predictions = app.bank.predict(req)

    locs = [{
        "lat": station.coords['lat'],
        "long": station.coords['long'],
    } for station in predictions.values()]

    url = "https://www.google.com/maps/dir"

    for coords in locs:
        url = f"{url}/{coords['lat']}+{coords['long']}"

    return {
        "res": url
    }



#find/?reqType=1&lat=-100&long=2&k=10
@app.get("/find/")
async def findStations(reqType:int, lat:float, long:float, k:int=10):
    type = requestType[reqType]
    req = Request(lat,long,type)

    return {
        "res": app.bank.predict(req)
    }

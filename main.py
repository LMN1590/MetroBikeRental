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

#/route/?startLat=34&startLong=-118&endLat=34.2&endLong=-118.5&slots=10
@app.get("/route/")
async def routing(startLat:float, startLong:float, endLat:float, endLong:float, slots:int):
    req = createRoutingReq(startLat,startLong,endLat,endLong,slots)
    predictions = app.bank.predict(req)
    locs = outputFormat(predictions)
    url = urlFormatting(locs)
    return {
        'status': predictions['status'],
        "data": url
    }

def createRoutingReq(startLat:float, startLong:float, endLat:float, endLong:float, slots:int):
    startLoc = {
        'lat': startLat,
        'long': startLong
    }
    endLoc = {
        'lat': endLat,
        'long': endLong
    }
    req = RoutingRequest(startLoc,endLoc,slots)
    return req

def outputFormat(predictions):
    locs = [{
        "lat": station.coords['lat'],
        "long": station.coords['long'],
    } for station in predictions['data'].values()]
    return locs

def urlFormatting(locs):
    url = "https://www.google.com/maps/dir"

    for coords in locs:
        url = f"{url}/{coords['lat']}+{coords['long']}"
    url = url + "/data=!3m1!4b1!4m10!4m9!1m3!2m2!1d-118!2d34!1m3!2m2!1d-118.5!2d34.2!3e2"

    return url




#find/?reqType=1&lat=-100&long=2&k=10&slots=1
@app.get("/find/")
async def findStations(reqType:int, lat:float, long:float, slots:int, k:int=10):
    type = requestType[reqType]
    req = Request(lat,long,type,slots,k)

    predictions = app.bank.predict(req)

    return predictions

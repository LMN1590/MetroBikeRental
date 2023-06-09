from typing import Union
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

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

#http://127.0.0.1:8000/route/?startLat=34&startLong=-118&endLat=34.2&endLong=-118.5&slots=1
@app.get("/route/")
async def routing(startLat:float, startLong:float, endLat:float, endLong:float, slots:int):
    req = createRoutingReq(startLat,startLong,endLat,endLong,slots)
    predictions = app.bank.predict(req)
    
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
    }

    return JSONResponse(content=jsonable_encoder(predictions), headers=headers)



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



#http://127.0.0.1:8000/find/?reqType=1&lat=34.035758&long=-118.266344&k=2&slots=1
#Unreachable: http://127.0.0.1:8000/find/?reqType=1&lat=33.795658&long=-118.266344&k=2&slots=1
@app.get("/find/")
async def findStations(reqType:int, lat:float, long:float, slots:int, k:int=10):
    type = requestType[reqType]
    req = Request(lat,long,type,slots,k)

    predictions = app.bank.predict(req)
    predictions['start'] = {
        "lat": lat,
        "long": long
    }

    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
    }

    return JSONResponse(content=jsonable_encoder(predictions), headers=headers)

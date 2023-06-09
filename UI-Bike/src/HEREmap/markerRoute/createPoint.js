import execMarker from "../execMarker/execMarker"

import startMarkerImg from '/startMarker.png';
import endMarkerImg from '/endMarker.png';
import markerImg from '/marker.png';
import routeImg from '/route.png';

import size from '../size/size.json'
export default function createMarkerRoute(data){
    let markerList = []

    const startLocCoord = data.startLoc.coords;
    const paramsStart = {
        "coords": startLocCoord,
        'name': "Starting Location",
        'time': 0
    }
    const startLoc = execMarker(paramsStart, startMarkerImg, size.marker,true);

    const endLocCoord = data.endLoc.coords;
    const paramsEnd = {
        "coords": endLocCoord,
        'name': "Ending Location",
        'time': data.startStation.time + data.endStation.time + data.routing.data.time
    }
    const endLoc = execMarker(paramsEnd, endMarkerImg, size.marker,true);

    markerList.push(startLoc,endLoc);
    const toStartStation = data.startStation.time
    const toEndStation = data.startStation.time + data.routing.data.time
    markerList.push(...processLoc(data.startStation, toStartStation), ...processLoc(data.endStation, toEndStation));
    markerList.push(...processRoute(data.routing.data.route));

    return markerList;
}

function processLoc(station, time){
    let markerList = []
    const params = {
        'coords': station.coords,
        'name': station.name,
        'time': time,
        'util': station.utilAvailable,
    }
    const dest = execMarker(params, markerImg, size.marker,true);
    markerList.push(dest);

    const routeParts = station.route;
    markerList.push(...processRoute(routeParts));
    

    return markerList;
}

function processRoute(route){
    let markerList = []

    const routeParts = route.parts;
    if(routeParts){
        for (const part of routeParts){
            const routeMarker = part.coords.map(coord => {
                const params = {
                    'coords':{
                        'lat': coord.lat,
                        'long': coord.lng
                    }
                }
                return execMarker(params, routeImg, size.route,false)
            });
            markerList.push(...routeMarker)
        }
    }

    return markerList;
}
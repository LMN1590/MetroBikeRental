import execMarker from "../execMarker/execMarker"

import startMarkerImg from '/startMarker.png';
import endMarkerImg from '/endMarker.png';
import markerImg from '/marker.png';
import routeImg from '/route.png';

import size from '../size/size.json'
export default function createMarkerRoute(data){
    let markerList = []

    const startLocCoord = data.startLoc.coords;
    const startLoc = execMarker(startLocCoord.lat, startLocCoord.long, startMarkerImg, size.marker);

    const endLocCoord = data.endLoc.coords;
    const endLoc = execMarker(endLocCoord.lat, endLocCoord.long, endMarkerImg, size.marker);

    markerList.push(startLoc,endLoc);
    
    markerList.push(...processLoc(data.startStation), ...processLoc(data.endStation));
    markerList.push(...processRoute(data.routing.data.route));

    return markerList;
}

function processLoc(station){
    let markerList = []

    const dest = execMarker(station.coords.lat, station.coords.long, markerImg, size.marker);
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
            const routeMarker = part.coords.map(coord => execMarker(coord.lat, coord.lng, routeImg, size.route));
            markerList.push(...routeMarker)
        }
    }

    return markerList;
}
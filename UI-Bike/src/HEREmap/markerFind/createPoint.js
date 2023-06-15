import execMarker from "../execMarker/execMarker"

import startMarker from '/startMarker.png';
import marker from '/marker.png';
import route from '/route.png';

import size from '../size/size.json'

function calcEuclid(coord1,coord2, threshhold){
    const diffLat = coord1.lat - coord2.lat;
    const diffLng = coord1.lng - coord2.lng;
    return Math.sqrt(diffLat**2 + diffLng**2) > threshhold;
}

export default function createMarkerFind(data, start){
    let markerList = []
    for(const station of data){
        const params = {
            'coords': station.coords,
            'name': station.name,
            'time': station.time,
            'util': station.utilAvailable,
        }
        const dest = execMarker(params, marker, size.marker, true);
        const routeParts = station.route.parts;
        if(routeParts){
            for (const part of routeParts){
                let prev = undefined;
                for (const coord of part.coords){
                    const params = {
                        'coords': {
                            'lat': coord.lat,
                            'long': coord.lng
                        }
                    }
                    if(!prev){
                        prev = params
                        markerList.push(execMarker(params, route, size.route, false))
                    }
                    else{
                        if(calcEuclid(params.coords, prev.coords, 0.00001)){
                            markerList.push(execMarker(params, route, size.route, false))
                            prev = params
                        }
                    }
                }
            }
        }
        markerList.push(dest);

    }
    const params = {
        'coords': start
    }
    markerList.push(execMarker(params,startMarker,size.marker,true));

    return markerList;
}






import execMarker from "../execMarker/execMarker"

import startMarker from '/startMarker.png';
import marker from '/marker.png';
import route from '/route.png';

import size from '../size/size.json'

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
                const routeMarker = part.coords.map(coord => {
                    const params = {
                        'coords': {
                            'lat': coord.lat,
                            'long': coord.lng
                        }
                    }
                    return execMarker(params, route, size.route, false)
                });
                markerList.push(...routeMarker)
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






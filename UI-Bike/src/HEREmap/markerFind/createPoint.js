import execMarker from "../execMarker/execMarker"

import startMarker from '/startMarker.png';
import marker from '/marker.png';
import route from '/route.png';

import size from '../size/size.json'

export default function createMarkerFind(data, start){
    let markerList = []
    for(const station of data){
        
        const dest = execMarker(station.coords.lat, station.coords.long, marker, size.marker);
        const routeParts = station.route.parts;
        if(routeParts){
            for (const part of routeParts){
                const routeMarker = part.coords.map(coord => execMarker(coord.lat, coord.lng, route, size.route));
                markerList.push(...routeMarker)
            }
        }
        markerList.push(dest);

    }
    markerList.push(execMarker(start.lat,start.long,startMarker,size.marker));
    return markerList;
}






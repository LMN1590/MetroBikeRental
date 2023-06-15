import data from '../data/data.json'

import marker from '/marker.png';

import size from './size/size.json';

import execMarker from './execMarker/execMarker'

export default function testStation(){
    const stations = data.features.map(el => {
        const params = {
            "coords":{
                "lat": el.geometry.coordinates[1],
                'long': el.geometry.coordinates[0]
            },
            "name": el.properties.name,
            "util":{
                "bikesAvailable": el.properties.bikesAvailable,
                "docksAvailable": el.properties.docksAvailable
            }
        }
        return execMarker(params, marker, size.marker, true)
    })
    return stations;
}
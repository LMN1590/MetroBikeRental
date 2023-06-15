import $ from 'jquery';

import markerImg from '/testMarker.png';

import size from './size/size.json';

import execMarker from './execMarker/execMarker'

function getData(){
    const URL="https://bikeshare.metro.net/stations/json/";

    return $.get({
        url: URL,
        crossDomain: true,
    });
}


function formatToMarker(data){
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
        const marker = execMarker(params, markerImg, size.marker, true);
        marker.setZIndex(100);
        return marker;
    })
    return stations;
}

export default function testStation(){
    return getData().then(
        formatToMarker
    )
}
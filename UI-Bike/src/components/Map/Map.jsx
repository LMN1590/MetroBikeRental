import React from "react";

import "./Map.css"
import data from '../../data/data.json'

import initMap from "../../HEREmap/initmap";
import createMarker from "../../HEREmap/createMarker";
import addMarker from "../../HEREmap/addMarker";

export default function Map({res,setRes}){
    const [markers, setMarkers] = React.useState([]);
    return(
        <div className="map" id="mapContainer">
            
        </div>
        
    )
}
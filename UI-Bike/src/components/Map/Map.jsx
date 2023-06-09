import React from "react";

import "./Map.css"

import initMap from "../../HEREmap/initmap";
import createMarker from "../../HEREmap/createMarker";


export default function Map({res,setRes}){
    const [markers, setMarkers] = React.useState(undefined);
    const [ready, setReady] = React.useState(false);

    const map = React.useMemo(()=>{
        try {
            return initMap();
        } catch (error) {
            console.log(error);
            return undefined;
        }
        
    },[ready])

    React.useEffect(() => {
        setReady(true);
    },[])

    React.useEffect(() => {
        if(res){
            const status = res.status;
            if(!status){
                alert("Can't find Route");
            }
            else{
                if(markers){
                    map.removeObjects(markers);
                }
                setMarkers(createMarker(res));
            }
        }
    },[res])

    React.useEffect(() => {
        if(map){

            map.addObjects(markers);
        }
    },[markers])
    return(
        <div className="map" id="mapContainer">
            
        </div>
        
    )
}
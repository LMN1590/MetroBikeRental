import React from "react";

import "./Map.css"

import initMap from "../../HEREmap/initmap";
import createMarker from "../../HEREmap/createMarker";
import testStation from "../../HEREmap/test";


export default function Map({res,setRes,test,setTest}){
    const [markers, setMarkers] = React.useState(undefined);
    const [ready, setReady] = React.useState(false);
    const [testList, setTestList] = React.useState(undefined);
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
        testStation().then(
            res => setTestList(res)
        )
    },[])

    React.useEffect(() => {
        if(res){
            const status = res.status;
            if(!status){
                alert("Can't resolve request");
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

    React.useEffect(() => {
        if(map){
            if(testList){
                if(test){
                    map.addObjects(testList);
                }
                else{
                    map.removeObjects(testList);
                }
            }
        }
    },[test])
    return(
        <div className="map" id="mapContainer">
            
        </div>
        
    )
}
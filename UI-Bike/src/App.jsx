import React from "react";

import Query from "./components/Query/Query";
import Map from "./components/Map/Map";

import './App.css'

function getLoc(locObj){
    localStorage.setItem('location', `${locObj.coords.latitude},${locObj.coords.longitude}`);
}

export default function App(){
    navigator.geolocation.getCurrentPosition(getLoc);
    const location=localStorage.getItem('location');

    const [res,setRes] = React.useState(location);
    return (
        <div className="main">
            <Query res={res} setRes={setRes}/>
            <Map res={res} setRes={setRes}/>
        </div>
    )
}
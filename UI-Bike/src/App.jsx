import React from "react";

import Query from "./components/Query/Query";
import Map from "./components/Map/Map";

import './App.css'

export default function App(){
    return (
        <div className="main">
            <Query/>
            <Map/>
        </div>
    )
}
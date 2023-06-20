import React from "react";

import Query from "./components/Query/Query";
import Map from "./components/Map/Map";

import './App.css'

export default function App(){
    const [res,setRes] = React.useState(undefined);
    const [testBool,setTest] = React.useState(false);
    return (
        <div className="main">
            <Query res={res} setRes={setRes} test={testBool} setTest={setTest}/>
            <Map res={res} setRes={setRes} test={testBool} setTest={setTest}/>
        </div>
    )
}
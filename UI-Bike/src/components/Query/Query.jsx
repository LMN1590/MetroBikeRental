import React from "react";

import './Query.css'

import getFind from "../../localAPI/getFind/getFind";
import getRoute from "../../localAPI/getRoute/getRoute";

export default function Query({res,setRes}){
    /////////////////////////////////////////////////////////////////////////////////////
    const findTitle = 'Request/Return Bike';
    const routeTitle = 'Routing'
    const [find, setFind] = React.useState({
        "Latitude": 34.035758,
        "Longitude": -118.266344,
        "K": 2,
        "Slots": 1,
        "Type": 1
    })
    const [route, setRoute] = React.useState({
        "Starting Latitude": 34.035458,
        "Starting Longitude": -118.266344,
        "Ending Latitude": 34.035758,
        "Ending Longitude": -118.296344,
        "Slots": 1
    })
    const [index,setIndex] = React.useState(0);
    /////////////////////////////////////////////////////////////////////////////////////
    
    const findKeys = Object.keys(find);
    const findForm = findKeys.map(el => {
        return (
            <div key={el}>
                <label htmlFor={el}>{el}</label>
                <input type="number" value={find[el]} onChange={event => {
                    setFind(prev => {
                        const newBody = {
                            ...prev
                        };
                        newBody[el] = event.target.value;
                        return newBody;
                    })
                }}/>
            </div>
        )
    })
    /////////////////////////////////////////////////////////////////////////////////////
    const routeKeys = Object.keys(route);
    const routeForm = routeKeys.map(el => {
        return (
            <div key={el}>
                <label htmlFor={el}>{el}</label>
                <input type="number" value={route[el]} onChange={event => {
                    setRoute(prev => {
                        const newBody = {
                            ...prev
                        };
                        newBody[el] = event.target.value;
                        return newBody;
                    })
                }}/>
            </div>
        )
    })
    /////////////////////////////////////////////////////////////////////////////////////
    const curForm = (index==0)?findForm:routeForm;
    const curTitle = (index==0)?findTitle:routeTitle;
    /////////////////////////////////////////////////////////////////////////////////////
    

    function execSubmit(){
        const func = (index == 0)?getFind:getRoute;
        const curVal = (index == 0)?find:route;

        func(curVal).then((ret)=>{
            setRes(ret);
        })
    }




    return(
        <div className="query">
            <div className="header">
                <div className="left-arrow" onClick={_ => {setIndex(prev => (prev+1)%2)}}>
                    <i className="fa-solid fa-arrow-left"></i>
                </div>
                <div className="title">{curTitle}</div>
                <div className="right-arrow" onClick={_ => {setIndex(prev => (prev+1)%2)}}>
                    <i className="fa-solid fa-arrow-right"></i>
                </div>
            </div>
            <div className="body">
                <form action="#">
                    {curForm}
                </form>
                <button onClick={execSubmit}>Submit</button>
            </div>
        </div>
    )
}
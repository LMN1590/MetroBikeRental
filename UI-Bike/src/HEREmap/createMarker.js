import createMarkerFind from "./markerFind/createPoint";
import createMarkerRoute from "./markerRoute/createPoint";

export default function createMarker(res){
    const type = res.type;
    if(type == "docking" || type =='renting'){
        return createMarkerFind(res.data, res.start);
    }
    else if(type == "routing"){
        return createMarkerRoute(res.data);
    }
}
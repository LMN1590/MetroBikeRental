import apiCallForRoute from "./apiCall";

export default async function getRoute(params){
    const startLat = parseFloat(params['Starting Latitude']);
    const startLong = parseFloat(params['Starting Longitude']);
    const endLat = parseFloat(params['Ending Latitude']);
    const endLong = parseFloat(params['Ending Longitude']);
    const slots = parseFloat(params.Slots);

    const newParams = {
        startLat,
        startLong,
        endLat,
        endLong,
        slots,
    }

    return await apiCallForRoute(newParams)
}
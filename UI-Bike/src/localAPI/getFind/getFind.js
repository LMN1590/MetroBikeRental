import apiCallForFind from "./apiCall";

export default async function getFind(params){
    const k = parseFloat(params.K);
    const lat = parseFloat(params.Latitude);
    const long = parseFloat(params.Longitude);
    const slots = parseFloat(params.Slots);
    const reqType = parseFloat(params.Type);

    const newParams = {
        k,
        lat,
        long,
        slots,
        reqType
    }

    return await apiCallForFind(newParams)
}
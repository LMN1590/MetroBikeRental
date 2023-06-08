export default function initMap(){
    const apikey = 'K177Fw63831tLMIveyyOH1-gkTxLlxyEdwyRDmidt2k'
    var platform = new H.service.Platform({
        apikey: apikey
    });
    var defaultLayers = platform.createDefaultLayers();

    var map = new H.Map(document.getElementById('mapContainer'), defaultLayers.vector.normal.map, {
        center: {lat: 52.496, lng: 13.382},
        zoom: 11,
        pixelRatio: window.devicePixelRatio || 1
    });
    window.addEventListener('resize', () => map.getViewPort().resize());
    var behavior = new H.mapevents.Behavior(new H.mapevents.MapEvents(map));
    return map
}
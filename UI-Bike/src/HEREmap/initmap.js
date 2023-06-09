export default function initMap() {
    const apikey = 'K177Fw63831tLMIveyyOH1-gkTxLlxyEdwyRDmidt2k'
    var platform = new H.service.Platform({
        apikey: apikey
    });
    var defaultLayers = platform.createDefaultLayers();

    var map = new H.Map(document.getElementById('mapContainer'), defaultLayers.vector.normal.map, {
        center: { lat: 34.0485, lng: -118.25854 },
        zoom: 10,
        pixelRatio: window.devicePixelRatio || 1
    });
    // add a resize listener to make sure that the map occupies the whole container
    window.addEventListener('resize', () => map.getViewPort().resize());

    // MapEvents enables the event system
    // Behavior implements default interactions for pan/zoom (also on mobile touch environments)
    var behavior = new H.mapevents.Behavior(new H.mapevents.MapEvents(map));

    // create default UI with layers provided by the platform
    var ui = H.ui.UI.createDefault(map, defaultLayers);

    var group = new H.map.Group();

    map.addObject(group);
    // add 'tap' event listener, that opens info bubble, to the group
    group.addEventListener('tap', function (evt) {
        // event target is the marker itself, group is a parent event target
        // for all objects that it contains
        var bubble = new H.ui.InfoBubble(evt.target.getGeometry(), {
            // read custom data
            content: evt.target.getData()
        });
        // show info bubble
        ui.addBubble(bubble);
    }, false);
    return group
}
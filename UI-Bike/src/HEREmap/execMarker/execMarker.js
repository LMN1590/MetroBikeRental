export default function execMarker(params, img, size, prio) {
    // Create an icon, an object holding the latitude and longitude, and a marker:
    var icon = new H.map.Icon(img, { size: size })

    var marker = new H.map.Marker({ lat: params.coords.lat, lng: params.coords.long }, { icon: icon });
    let time = 0;
    if(params.time){
        if(params.time >=3600 ) time = new Date(params.time * 1000).toISOString().substring(11, 16)
        else time = new Date(params.time * 1000).toISOString().substring(14, 19)
    }
    const html =
        (params.name ? `
        <div class="name">
            <span>${params.name}</span>
        </div>
        `: ``) +
        (params.time ? `
        <div class="time">
            ${time}
        </div>
        `: ``) +
        (params.util ? `
        <p>
            Utilities
        </p>
        <div class="bikes">
            -  ${params.util.bikesAvailable} bikes left
        </div>
        <div class="docks">
            -  ${params.util.docksAvailable} docks left
        </div>
        `: ``);
    console.log(html);
    marker.setData(html);
    if (prio) {
        marker.setZIndex(999);
    }
    else {
        marker.setZIndex(1);
    }
    return marker;
}
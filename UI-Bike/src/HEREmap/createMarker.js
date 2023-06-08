export default function createMarker(lat,lng){
    var svgMarkup = '<svg width="24" height="24" ' +
    'xmlns="http://www.w3.org/2000/svg">' +
    '<rect stroke="white" fill="#1b468d" x="1" y="1" width="22" ' +
    'height="22" /><text x="12" y="18" font-size="12pt" ' +
    'font-family="Arial" font-weight="bold" text-anchor="middle" ' +
    'fill="white">H</text></svg>';

    // Create an icon, an object holding the latitude and longitude, and a marker:
    var icon = new H.map.Icon(svgMarkup)

    var marker = new H.map.Marker({lat: lat, lng: lng}, { icon: icon });
    return marker;
}
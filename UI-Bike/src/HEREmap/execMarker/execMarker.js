export default function execMarker(lat,lng, img, size){
    // Create an icon, an object holding the latitude and longitude, and a marker:
    var icon = new H.map.Icon(img, { size: size })

    var marker = new H.map.Marker({lat: lat, lng: lng}, { icon: icon });

    return marker;
}
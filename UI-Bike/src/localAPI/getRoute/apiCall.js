import $ from "jquery";

export default function apiCallForRoute(params){
    const URL="http://127.0.0.1:8000/route/";

    return $.get({
        url: URL,
        crossDomain: true,
        data: {
            ...params
        },
        contentType: 'text/plain',
    });
}
import $ from "jquery";

export default function apiCallForFind(params){
    const URL="http://127.0.0.1:8000/find/";

    return $.get({
        url: URL,
        crossDomain: true,
        data: {
            ...params
        },
        contentType: 'text/plain',
    });
}
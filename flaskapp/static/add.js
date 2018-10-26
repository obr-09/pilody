var gui_url = document.getElementsByTagName('body')[0].getAttribute('data-url');
var base_url = gui_url.replace(/\/?gui\/?/, '');


$('#keyboard').jkeyboard({
    layout: 'english',
    input: $('#searchField')
});


function addResource() {
    var uriRegex = /^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$/gm;
    var search = $('#searchField').val();
    var isUri = search.match(uriRegex);
    if (isUri !== null) {
        var xhttp = new XMLHttpRequest();
        xhttp.open('POST', base_url + '/playlist', true);
        xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xhttp.send('playlist_url=' + encodeURI(search));
        xhttp.onreadystatechange = function() {
            $('#searchField').val('');
        };
    } else {

    }
}

var gui_url = document.getElementsByTagName('body')[0].getAttribute('data-url');
var base_url = gui_url.replace(/\/?add\/?/, '');


$('#keyboard').jkeyboard({
    layout: 'english',
    input: $('#searchField')
});


function addResource() {
    var search = $('#searchField').val();
    var xhttp = new XMLHttpRequest();
    xhttp.open('POST', base_url + '/music', true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send('youtube_url=' + encodeURIComponent(search));
    xhttp.onreadystatechange = function() {
        if (xhttp.status >= 400) {
            xhttp = new XMLHttpRequest();
            xhttp.open('POST', base_url + '/playlist', true);
            xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
            xhttp.send('playlist_url=' + encodeURIComponent(search));
            xhttp.onreadystatechange = function() {
                $('#searchField').val('');
            };
        } else {
            $('#searchField').val('');
        }
    };
}

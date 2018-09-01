var gui_url = document.getElementsByTagName('body')[0].getAttribute('data-url');
var base_url = gui_url.replace(/\/?gui\/?/, '');


function play() {
    var xhttp = new XMLHttpRequest();
    xhttp.open('POST', base_url + '/control', true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send('action=pause');
}

function previous() {
    var xhttp = new XMLHttpRequest();
    xhttp.open('POST', base_url + '/control', true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send('action=previous');
}

function next() {
    var xhttp = new XMLHttpRequest();
    xhttp.open('POST', base_url + '/control', true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send('action=next');
}
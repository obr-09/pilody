var gui_url = document.getElementsByTagName('body')[0].getAttribute('data-url');
var base_url = gui_url.replace(/\/?gui\/?/, '');


var playTriggered = false;
function play() {
    if (playTriggered) {
        return;
    }
    var xhttp = new XMLHttpRequest();
    xhttp.open('POST', base_url + '/control', true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.onreadystatechange = function() {
        var buttonPlay = document.getElementById("button-play");
        playTriggered = true;
        buttonPlay.classList.add((xhttp.status / 100 === 2) ? "button-success" : "button-error");
        setTimeout(function() {
            buttonPlay.classList.remove("button-success", "button-error");
            playTriggered = false;
        }, 1000);
    };
    xhttp.send('action=pause');
}


var previousTriggered = false;
function previous() {
    if (previousTriggered) {
        return;
    }
    var xhttp = new XMLHttpRequest();
    xhttp.open('POST', base_url + '/control', true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.onreadystatechange = function() {
        var buttonPrevious = document.getElementById("button-previous");
        previousTriggered = true;
        buttonPrevious.classList.add((xhttp.status / 100 === 2) ? "button-success" : "button-error");
        setTimeout(function() {
            buttonPrevious.classList.remove("button-success", "button-error");
            previousTriggered = false;
        }, 1000);
    };
    xhttp.send('action=previous');
}


var nextTriggered = false;
function next() {
    if (nextTriggered) {
        return;
    }
    var xhttp = new XMLHttpRequest();
    xhttp.open('POST', base_url + '/control', true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.onreadystatechange = function() {
        var buttonNext = document.getElementById("button-next");
        nextTriggered = true;
        buttonNext.classList.add((xhttp.status / 100 === 2) ? "button-success" : "button-error");
        setTimeout(function() {
            buttonNext.classList.remove("button-success", "button-error");
            nextTriggered = false;
        }, 1000);
    };
    xhttp.send('action=next');
}


setInterval(getMusic, 250);
function getMusic() {
    var xhttp = new XMLHttpRequest();
    xhttp.open('GET', base_url + '/music', true);
    xhttp.onreadystatechange = function() {
        try {
            var musicInfo = JSON.parse(xhttp.responseText);
            Array.prototype.forEach.call(document.getElementsByClassName("music-name"), function(element) {
                element.innerHTML = musicInfo.title;
            });
            Array.prototype.forEach.call(document.getElementsByClassName("music-artist"), function(element) {
                element.innerHTML = musicInfo.artist;
            });
        } catch (e) {
            console.log(e);
        }
    };
    xhttp.send();
}

var gui_url = document.getElementsByTagName('body')[0].getAttribute('data-url');
var base_url = gui_url.replace(/\/?add\/?/, '');


$('#keyboard').jkeyboard({
    layout: 'english',
    input: $('#searchField')
});


function addResource() {
    var searchField = $('#searchField');
    var search = searchField.val();
    var xhttp = new XMLHttpRequest();
    xhttp.open('POST', base_url + '/music', true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.onreadystatechange = function() {
        if (xhttp.status >= 400) {
            xhttp2 = new XMLHttpRequest();
            xhttp2.open('POST', base_url + '/playlist', true);
            xhttp2.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
            xhttp2.onreadystatechange = function() {
                if (xhttp2.status < 400) {
                    searchField.addClass('success');
                    $('#searchMessage').text('Playlist set.');
                    setTimeout(function() {
                        searchField.removeClass('success');
                    }, 1000);
                } else {
                    searchField.addClass('error');
                    $('#searchMessage').text('Not found.');
                    setTimeout(function() {
                        searchField.removeClass('error');
                    }, 1000);
                }
                searchField.val('');
            };
            searchField.addClass('progress');
            $('#searchMessage').text('Searching playlist...');
            xhttp2.send('playlist_url=' + encodeURIComponent(search));
        } else {
            $('#searchMessage').text('Music set.');
            searchField.val('');
            setTimeout(function() {
                searchField.removeClass('success');
            }, 1000);
        }
    };
    searchField.addClass('progress');
    $('#searchMessage').text('Searching music...');
    xhttp.send('youtube_url=' + encodeURIComponent(search));
}

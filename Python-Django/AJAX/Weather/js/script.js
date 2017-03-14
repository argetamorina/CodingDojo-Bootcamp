$(document).ready(function(){
    $('.search').submit(function(event){
        var name = $('.name').val();
        var url = 'http://api.openweathermap.org/data/2.5/weather?q=' + name + '&APPID=c82ebeea21774b168a350cf28ba3592b&units=imperial';
        var element = '';
        $.getJSON(url, null, function(response){
            element += '<h1>' + response.name + '</h1>',
                element += '<p>' + response.main.temp + '</p>';
            $('.data').html(element);
        });
        event.preventDefault();
    });
})

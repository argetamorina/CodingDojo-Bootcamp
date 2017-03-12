$(document).ready(function(){
     $('img').hover(function(){
		var srcValue = $(this).attr('data-alt-src'); 
        var dataValue = $(this).attr('src');
        	$(this).attr('src', srcValue);
        	$(this).attr('data-alt-src', dataValue);
     });
});
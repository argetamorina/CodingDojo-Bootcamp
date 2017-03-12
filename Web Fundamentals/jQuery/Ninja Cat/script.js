$(document).ready(function(){
	$('div').sortable();
	$('img').on({'click': function(){
    	var srcValue = $(this).attr('data-alt-src'); 
        var dataValue = $(this).attr('src'); 
        $(this).attr('src', srcValue);
        $(this).attr('data-alt-src', dataValue);
      	 // $('img').sortable();

    	}
	});
});
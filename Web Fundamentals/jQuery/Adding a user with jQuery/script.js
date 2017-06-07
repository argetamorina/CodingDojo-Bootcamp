$(document).ready(function() {
	$('form').submit(function(){
		$('#table1').append('<tr><td>' + $('#input1').val() + '</td><td>' + $('#input2').val() + '</td><td>' + $('#input3').val() + '</td><td>' + $('#input4').val() + '</td></tr>'  );

		return false;
	});
});
 $(document).ready(function() {
 	// $(document).mousemove(function (e) {
 	// 	$('.square').css({
 	// 		top: e.offsetY,
 	// 		left: e.offsetX
 	// 	});
 	// });
 	$('h1').click(function() {
 		alert(" You click me!!!");
 	})

 	$( "#input1" ).focus(function(){
  		alert( "Handler for .focus() called." );
	});
	$( "p" ).addClass( "newClass" );

	function displayVals() {
  		var values = $( "#numberValue" ).val();
  		 $( '#displayAnswer' ).html( "<b>Price:</b> " + values);
	}
	displayVals();

	$('#text').text('We add some text .text()');

	var title = $( "em" ).attr( "title" );
	$( ".atr" ).text( title );

	$( ".data" ).data( "test", { first: "the game", last: "go home now" } );
	$( "span:first" ).text( $( ".data" ).data( "test" ).first );
	$( "span:last" ).text( $( ".data" ).data( "test" ).last );
	 });

 	$("#testp").hide();
  	$( "#t4est" ).click(function() {
  	$( "#testp" ).show( "slow");
  	});

	$( "#clickme" ).click(function() {
  	$( "#img" ).hide( "slow", function() {
    	alert( "Animation complete." );
 	});


  	// $('#toggle').click( function() {
  	// 	$('#toggle-text').toggle( ) ;

  	// });

  	$('#toggle').click(function(){
				$('#data #img1').toggle();
				console.log("Clicked the button to show or hide the image.");
			});
			$('#fadeIn').click(function(){
				$('#img1').fadeIn("slow");
				console.log("Clicked the button to fade in the image.");				
			});	
			$('#fadeOut').click(function(){
				$('#img1').fadeOut("slow");
				console.log("Clicked the button to fade out the image.");				
			});




 });
$(document).ready(function(){

	var world = [
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
		[0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
		[0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
		[0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
		[0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
		[0, 1, 0, 1, 1, 1, 9, 0, 1, 0],
		[0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
		[0, 1, 1, 1, 1, 1, 4, 1, 1, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	];

	function drawMap() {
		$('#map').html('');
		for(var row = 0; row < world.length; row++) {
			for (var col = 0; col < world[row].length; col++) {
				var html_str = "";
				if(world[row][col] === 1) {
					html_str = "<div class='path'></div>";
				} else if(world[row][col] === 0) {
					html_str = "<div class='wall'></div>";
				} else if (world[row][col] === 9) {
					html_str = "<div class='pacman'></div>";
				} else if (world[row][col] === 2) {
					html_str = "<div class='blank'></div>";
				}else if (world[row][col] === 3) {
					html_str = "<div class='cherry'></div>";
				}else if (world[row][col] === 4) {
					html_str = "<div class='ghost'></div>";
				}
				$('#map').append(html_str);
			}
		}
	};
	drawMap();

		var pacman = {
			row: 6,
			col: 6
		}
		var calories = 0;
		 var firstMoveMade = false;

	$('body').keydown(function(event){
		if(firstMoveMade === false) {
			setTimeout(function(){
				world[1][1] = 3;
				}, 3000);

			firstMoveMade = true;
		}
		// left arrow
		if (event.keyCode === 37) {

			if (world[pacman.row][pacman.col - 1] >= 1) {
				if (world[pacman.row][pacman.col - 1] === 1) {
					calories += 2000;
				}
				world[pacman.row][ pacman.col - 1] = 9;
				world[pacman.row][pacman.col] = 2;
				pacman.col--;
			}
		}
		// up arrow
		else if (event.keyCode === 38) {
			if (world[pacman.row - 1][pacman.col] >= 1) {
				if (world[pacman.row - 1][pacman.col] === 1) {
					calories += 2000;
				}
				world[pacman.row - 1][ pacman.col] = 9;
				world[pacman.row][pacman.col] = 2;
				pacman.row--;
			}
		}
		// right arrow
		else if (event.keyCode === 39) {
			if (world[pacman.row][pacman.col + 1] >= 1) {
				if (world[pacman.row][pacman.col + 1] === 1) {
					calories += 2000;
				}
				world[pacman.row][ pacman.col +1] = 9;
				world[pacman.row][pacman.col] = 2;
				pacman.col++;
			}
		}
		// down arrow
		else if (event.keyCode === 40) {
			if (world[pacman.row + 1][pacman.col] >= 1) {
				if (world[pacman.row + 1][pacman.col] === 1) {
					calories += 2000;
				}
				world[pacman.row + 1][pacman.col] = 9;
				world[pacman.row][pacman.col] = 2;
				pacman.row++;
			}
		}

		$('#calories').html('Calories: ' + calories);
		drawMap();
		
	});
});
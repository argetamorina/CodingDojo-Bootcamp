$(document).ready(function(){
    for (var i = 1; i < 152; i++) {
        $('.pokemons').append('<img id=' + i + ' src="http://pokeapi.co/media/img/' + i +'.png">');;
    }
    $(".pokemons img").on("click", function() {
        var id = $(this).attr("id"),
            src = $(this).attr("src");
        var url = "http://pokeapi.co/api/v1/pokemon/" + id + "/";

        $.getJSON(url, null, function(pokemon) {
            var pokedex = '';
            pokedex += '<div class="pokedex">';
                pokedex += '<h1 class="name">' + pokemon.name + '</h1>';

                pokedex += '<img class="image" src="'+ src +'">';

                pokedex += '<h3>Types</h3>';
                pokedex += '<ul class="types">';
                for (var i = 0; i < pokemon.types.length; i++) {
                    pokedex += '<li>' + pokemon.types[i].name + '</li>';
                }
                pokedex += '</ul>';

                pokedex += '<h3>Height</h3>';
                pokedex += '<span class="height">' + pokemon.height + '</span>';

                pokedex += '<h3>Weight</h3>';
                pokedex += '<span class="weight">' + pokemon.weight + '</span>';
            pokedex += '</div>';

            $('.pokedexes').append(pokedex);
        });
    });
})

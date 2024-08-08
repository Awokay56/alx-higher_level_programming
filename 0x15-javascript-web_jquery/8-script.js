$("#list_movies").empty(); 

  $.get("https://swapi-api.alx-tools.com/api/films/?format=json", function(data) {
    var movies = data.results;

    $.each(movies, function(index, movie) {
      var listItem = $("<li>" + movie.title + "</li>");
      $("#list_movies").append(listItem);
    });
  });

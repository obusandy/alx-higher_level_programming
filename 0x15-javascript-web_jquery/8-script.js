// Below is a script that movie titles
// must be list in the HTML tag UL#list_movies

$.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    datatype: 'json',
    success: function (data) {
        // gets the un ordered lists elements
        const movieTitles = data.results.map(function (movie) {
            return movie.title;
        })

        const listElement = $('UL#list_movies');
        // below is 
        // append
        $.each(movieTitles, function (index, title) {
            const listItem = $('<li>' + title + '</li>');
            listElement.append(listItem);
        })
    }
});

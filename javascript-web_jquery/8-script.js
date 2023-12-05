/* Wait for document to be read */
$(document).ready(function () {
  const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

  $.get(url, function (data) {
    for (let x = 0; x < data.results.length; x++) {
      $('UL#list_movies').append('<li>' + data.results[x].title + '</li>');
    }
  });
});

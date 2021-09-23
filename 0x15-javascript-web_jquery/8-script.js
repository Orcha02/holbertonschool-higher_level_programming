$(function () {
  const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
  $.get(url, function (data, status) {
    if (status === 'success') {
      const objects = data.results;
      objects.forEach((title) => {
        $('#list_movies').append(`<li>${title.title}</li>`);
      });
    }
  });
});

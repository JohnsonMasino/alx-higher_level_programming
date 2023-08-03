'use strict';
$(() => {
  const BASE_URL = 'https://swapi-api.hbtn.io/api';

  $.get(`${BASE_URL}/films/?format=json`, (data, status) => {
    data.results.forEach(film => {
      $('UL#list_movies').append(`<li>${film.title}</li>`);
    });
  });
});

'use strict';
$(() => {
  const BASE_URL = 'https://swapi-api.hbtn.io/api';

  $.get(`${BASE_URL}/people/5/?format=json`, (data, status) => {
    $('DIV#character').html(data.name);
  });
});

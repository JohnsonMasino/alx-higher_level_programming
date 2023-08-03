'use strict';
$(() => {
  const BASE_URL = 'https://fourtonfish.com';

  $.get(`${BASE_URL}/hellosalut/?lang=fr`, (data, status) => {
    $('DIV#hello').html(data.hello);
  });
});

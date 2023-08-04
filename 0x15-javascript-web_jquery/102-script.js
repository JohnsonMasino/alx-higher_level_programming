const endpoint = 'https://www.fourtonfish.com/hellosalut/?lang=';

$('document').ready(() => {
  $('INPUT#btn_translate').click(() => {
    const lang = $('INPUT#language_code').val();
    $.get(endpoint + lang, (data) => {
      $('DIV#hello').text(data.hello);
    });
  });
});

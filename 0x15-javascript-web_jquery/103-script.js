$('document').ready(() => {
  $('INPUT#btn_translate').click(translate);
  $('INPUT#language_code').focus(() => {
    $(this).keydown(e => {
      if (e.keyCode === 13) {
        translate();
      }
    });
  });
});

function translate () {
  const endpoint = 'https://www.fourtonfish.com/hellosalut/?lang=';
  const lang = $('INPUT#language_code').val();
  $.get(endpoint + lang, (data) => {
    $('DIV#hello').text(data.hello);
  });
}

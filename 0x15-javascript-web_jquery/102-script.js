$(document).ready(() => {
  $('#btn_translate').click(() => {
    $.ajax({
      url: 'https://www.fourtonfish.com/hellosalut/',
      type: 'GET',
      data: { lang: $('#language_code').val() },
      success: (translate) => {
        $('#hello').html(translate.hello);
      }
    });
  });
});

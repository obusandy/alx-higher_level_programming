// JavaScript script that fetches from https://hellosalut.stefanbohacek.dev/?lang=fr
// and displays the value of hello from that fetch in the HTML tag DIV#hello.
$.ajax({
      url: 'https://fourtonfish.com/hellosalut/?lang=fr',
      method: 'GET',
      dataType: 'json',
      success: function (data) {
        // Translates hellow from the dta fetched
        const translation = data.hello;
        // Display the translation of hello
        $('DIV#hello').text(translation);
      }
});

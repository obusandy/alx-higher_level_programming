// no jquery
// script that updates the text color
// of the <header> element to red (#FF0000):
$('document').ready(function () {
    $('DIV#add_item').click(() => {
        $('UL.my_list').append('<li>Item</li>');
    });
    $('DIV#remove_item').click(() => {
        $('UL.my_list li:last').remove();
    });
    $('DIV#clear_list').click(() => {
        $('UL.my_list').empty();

    });

});











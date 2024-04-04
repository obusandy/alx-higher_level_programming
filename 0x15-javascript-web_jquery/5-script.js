// JavaScript script that adds a <li> element to a list
// user clicks
$('DIV#add_item').click(()=>{
    $('UL.my_list').append('<li>Item</li>');
});

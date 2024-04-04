// script that toggles the class
// of the <header> element when the user clicks on the tag
$(document).ready(function() {
    // Div by ID
    const toggleDiv = $('DIV#toggle_header');
    const headerElement = $('header');
    // Event-handler
    toggleDiv.click(function () {
        headerElement.toggleClass('red green');
    });
});

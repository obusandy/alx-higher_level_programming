// script that updates the text color of
// the <header> element to red
$(document).ready(function() {

    // div by ID
    const redHeaderDiv = $('DIV#red_header');
    // event-handler
    redHeaderDiv.click(function() {
        const headerElement = $('header');
        // finds the element
        // check if header elemnt was found
        if (headerElement) {
            // set color red to the element
            headerElement.css('color', '#FF0000');
        } else {
            console.error('Header elemnet not found');
        }
    });
});

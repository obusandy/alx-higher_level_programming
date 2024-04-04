// script that adds the class red to the <header> element 
$(document).ready(function() {

    // Div is selected by ID
    const redHeaderDiv = $('DIV#red_header');
    // Event-Handler
    redHeaderDiv.click(function() {
        const headerElement = $('header');
        // locate the header elememnt
        // check if header elemt was found
        if (headerElement) {
            // addClass(red)
            headerElement.addClass('red');
        } else {
            console.error('Header elemnet not found');
        }
    });
});


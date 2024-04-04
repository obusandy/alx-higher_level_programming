// script that updates the text color of the <header> element
$(document).ready(function () {
  // jquery selector to get the element
  const element = $('header');

  if (element) {
    // set color red to the element
    element.css('color', '#FF0000');
  } else {
    console.error('Header element not found');
  }
});

// below , query select the element
const element = document.querySelector('header');

if (element) {
    // look if the element is
    // present and sets its color
    element.style.color = '#FF0000';
} else {
    console.error('Header element not found');
}

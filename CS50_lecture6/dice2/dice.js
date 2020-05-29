// Template for roll results
const template = Handlebars.compile(document.querySelector('#result').innerHTML);

document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#roll').onclick = () => {
        // Generate a random roll.
        const roll = Math.floor((Math.random() * 6) + 1);

        // Add roll result to DOM.
        const content = template({'value': roll});
        document.querySelector('#rolls').innerHTML += content;
    };
});
// JavaScript to handle accordion toggle
document.querySelectorAll('.accordion-button').forEach(button => {
    button.addEventListener('click', () => {
        const accordionCollapse = button.parentElement.nextElementSibling;

        accordionCollapse.classList.toggle('open');
    });
});

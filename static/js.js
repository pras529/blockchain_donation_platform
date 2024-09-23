document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('#verification-form');

    form.addEventListener('submit', (event) => {
        event.preventDefault();
        let formData = new FormData(form);
        // Perform form validation and AJAX submission
        console.log('Form data submitted:', formData);
    });
});

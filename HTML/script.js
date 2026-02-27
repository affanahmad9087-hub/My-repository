const btn = document.querySelector('.neon-button');

btn.addEventListener('click', function(e) {
    // Only toggle if the button isn't already active
    if (!this.classList.contains('is-active')) {
        this.classList.add('is-active');
    }
});

// Prevent the form from collapsing when clicking inside the inputs
document.querySelector('.login-form').addEventListener('click', function(e) {
    e.stopPropagation();
});
// Alert for product buttons
const buttons = document.querySelectorAll('.product button');

buttons.forEach(button => {
    button.addEventListener('click', () => {
        alert('Terima kasih telah membeli!');
    });
});

// Smooth scrolling for navbar links
document.querySelectorAll('.navbar a').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

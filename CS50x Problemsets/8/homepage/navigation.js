document.addEventListener("DOMContentLoaded", function() {
    const navLinks = {
        "Home": "index.html",
        "Reservation": "reservations.html",
        "about": "about.html",
        "Location": "location.html"
    };
    document.querySelectorAll(".nav-link").forEach(link => {
        const text = link.textContent.trim();
        if (navLinks[text]) {
            link.href = navLinks[text];
        }
    });
});


document.querySelector('form').addEventListener('submit', function(event) {
    event.preventDefault();
    Swal.fire({
        title: 'Success!',
        text: 'Form submitted successfully!',
        icon: 'success',
        confirmButtonText: 'OK'
    });
});

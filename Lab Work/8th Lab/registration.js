document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("registrationForm");
    const result = document.getElementById("result");

    form.addEventListener("submit", function (event) {
        event.preventDefault();

        const fullName = document.getElementById("fullname").value;
        const email = document.getElementById("email").value;
        const password = document.getElementById("password").value;

        result.textContent = `Full Name: ${fullName} | Email: ${email} | Password: ${"*".repeat(password.length)}`;
    });
});
document.getElementById("loginForm").addEventListener("submit", function(event) {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const errorMessage = document.getElementById("errorMessage");

    if (username.trim() === "" || password.trim() === "") {
        event.preventDefault(); // Prevent form submission
        errorMessage.textContent = "Both fields are required!";
    }
});
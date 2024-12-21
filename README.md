# SQL Injection Prevention Login System

This repository contains a simple login system with SQL injection prevention using parameterized queries. It demonstrates a basic Flask web application that prevents SQL injection attacks by using parameterized queries in Python with SQLite.

## Project Structure

- `login.html`: HTML file that contains the login form. Users can enter their username and password to log in.
- `SQLInjectionPrevention.py`: Python file that contains the SQLInjectionPrevention class to interact with the SQLite database securely, preventing SQL injection.
- `styles.css`: CSS file for styling the login form.
- `script.js`: JavaScript file for client-side validation of the form.

## Features

- **SQL Injection Prevention**: The Python code uses parameterized queries to protect against SQL injection attacks.
- **User Login**: Users can log in using a username and password.
- **Basic Frontend**: The HTML form is styled with CSS, and JavaScript performs basic client-side validation to ensure both fields are filled.

## Setup Instructions

1. **Clone the repository**:
   
   git clone https://github.com/yourusername/sql-injection-prevention.git

2. **Install Dependencies**: If you don't have Flask installed, run the following command:
   
   pip install Flask

3. **Set up the Database**:

   The SQLite database is automatically created when the app runs, but you can also manually initialize the tables by running the create_table method in SQLInjectionPrevention.py.

4. **Running the Application**: Run the Flask app with the following command:

   python app.py

5. Navigate to http://localhost:5000 in your browser to view the login page.

6. **Testing the Application**:

   Enter a username and password on the login form.
   The app will verify the credentials against the users table in the SQLite database.
   If the credentials are incorrect, an error message will be displayed.

**License**

This project is licensed under the MIT License - see the LICENSE file for details.

**Contributions**

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature-branch).
Create a new pull request.

**Acknowledgments**

Flask for the lightweight web framework.
SQLite for the database engine.
The project is an educational demonstration of SQL injection prevention in a simple web application.


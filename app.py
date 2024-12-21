from flask import Flask, render_template, request, redirect, url_for
from sql_injection_prevention import SQLInjectionPrevention

# Initialize the Flask app
app = Flask(__name__)

# Initialize the database
db = SQLInjectionPrevention('test.db')
db.create_table()
db.insert_user('admin', 'securepassword')  # Add a default admin user

# Define the root route to redirect to the login page
@app.route('/')
def index():
    return redirect(url_for('login'))

# Define the login route to handle GET and POST requests
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':  # Handle form submission
        username = request.form['username']
        password = request.form['password']
        user = db.find_user(username, password)  # Check credentials in the database
        if user:
            return f"Welcome, {username}!"
        else:
            return "Login failed. Invalid username or password."
    return render_template('login.html')  # Render the login form for GET requests

# Define the logout route to redirect back to the login page
@app.route('/logout')
def logout():
    return redirect(url_for('login'))

# Ensure the app runs only when executed directly
if __name__ == "__main__":
    app.run(debug=True)
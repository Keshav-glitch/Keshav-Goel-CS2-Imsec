from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Secret key for session management
app.secret_key = 'your_secret_key'

# Database connection
def connect_db():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='USER',  # Make sure to create a 'USER' database with a 'USER' table
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['usname']
    password = request.form['pwd']

    # Input validation
    if not username or not password:
        flash('Email and Password are required!', 'danger')
        return redirect(url_for('login_page'))
    
    if len(password) < 8:
        flash('Password must be at least 8 characters long', 'danger')
        return redirect(url_for('login_page'))
    
    # Connect to the database
    connection = connect_db()
    cursor = connection.cursor()
    
    # Check credentials
    cursor.execute("SELECT * FROM USER WHERE email=%s", (username,))
    user = cursor.fetchone()
    
    
    if user and check_password_hash(user['password'], password):
        flash('Login successful!', 'success')
        return redirect(url_for('welcome'))
    else:
        flash('Invalid credentials, please try again.', 'danger')
        return redirect(url_for('login_page'))

@app.route('/welcome')
def welcome():
    return "Welcome to your dashboard!"

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for, session
# Rendering a template means A template is rendered with specific data to produce a final document.
# (render_template, request, redirect, url_for, session) from Flask that are used for rendering templates, handling HTTP requests,managing sessions, and redirecting URLs.

from flask_mysqldb import MySQL
# MySQL class is imported from flask_mysqldb. It provides MySQL database integration with Flask.

import MySQLdb.cursors
# Contains cursors classes for MySQL

import re

# provides support for regular expressions.


app = Flask(__name__) # Refers to the current name of the module i.e. app


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskapp'
# Setting the configuration variables for the MySQL connection.
# Did this using MySQL workbench and phpmyadmin through wamp server.
# I have connected MySQL workbench and phpmyadmin. Created flaskapp database, in which I created users, and accounts tables to access.

mysql = MySQL(app)
app.secret_key = 'your secret key'
# Sets the secret key for the Flask application. The secret key is used for securely signing the session cookie.


@app.route('/') # is a decorator in Flask that maps the specified URL pattern to the following pattern.
@app.route('/login', methods=['GET', 'POST']) # is another decorator that maps the "/login" URL pattern to the following function code. It can handle both GET and POST requests.
def login():
    # Function to handle the root URL and the '/login' URL.
    # Decorates the login() function as a route handler for the root URL ("/") and the "/login" URL.It accepts both GET and POST requests.

    msg = '' # Initializing an empty string variable called 'msg'. It will be used for storing messages to be displayed in the templates.

    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        # Creates a cursor object using the connection attribute of the mysql object. The cursor will be used to execute SQL queries.

        cursor.execute('SELECT * FROM accounts WHERE username = % s AND password = % s', (username, password,))
        # Executes a SQL query to select rows from the 'accounts' table where the 'username' and 'password' match the values provided.
        # The %s placeholders are used to prevent SQL injection, and the values are passed as a tuple.
        
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            msg = 'Logged in successfully !'
            return render_template('index.html', msg=msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg=msg)


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = % s', (username,))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers !'
        elif not username or not password or not email:
            msg = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO accounts VALUES (NULL, % s, % s, % s)', (username, password, email,))
            mysql.connection.commit()
            msg = 'You have successfully registered !'
            # If all conditions are satisfied, it executes an SQL query to insert a new row with the provided data into the 'accounts' table, commits the changes, and sets the msg variable to indicate successful registration.

    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('register.html', msg=msg)


if "__main__" == __name__:
    app.run(debug=True)

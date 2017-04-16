from flask import Flask, render_template, request, redirect, flash, session
import re
# import the Connector function
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'secret'
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'mydb')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registration', methods=['POST'])
def register():
    email = request.form['email']
    confirm_password = request.form['confirm_password']
    password = request.form['password']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    data1 = {
        'email': email
    }
    email_db = mysql.query_db("SELECT email from registration where email = :email", data1)
    if email_db:
        flash('You are register')
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', request.form['email'])
    if match == None or len(password) < 8 or password != confirm_password or len(first_name) < 2 or len(last_name) < 2 :
        flash('Wrong!')
    else:
        # run validations and if they are successful we can create the password hash with bcrypt
        pw_hash = bcrypt.generate_password_hash(password)
        query = "INSERT INTO registration (first_name, last_name, email, pw_hash,  created_at, updated_at) VALUES(:first_name, :last_name, :email, :pw_hash, NOW(), NOW())"
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': email,
            'pw_hash': pw_hash
            }
        mysql.query_db(query, data)
        flash('You are register now. Log In')
    return redirect('/')
@app.route('/login', methods=['POST'])
def log():
    email = request.form['email_log']
    password = request.form['password_log']
    match =re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
    if match == None:
        ('Your email is wrong, Please check')
    user_query = "SELECT * FROM registration WHERE email = :email LIMIT 1"
    query_data = { 'email': email }
    user = mysql.query_db(user_query, query_data)

    if bcrypt.check_password_hash(user[0]['pw_hash'], password):
        return render_template('success.html')
    if not user[0]['email']:
        flash('You are not register. Please register.')
        return redirect('/')
app.run(debug=True)

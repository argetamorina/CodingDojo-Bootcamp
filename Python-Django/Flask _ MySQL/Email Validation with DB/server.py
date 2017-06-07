from flask import Flask, render_template, request, redirect, flash, session
import re
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'secret'
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'mydb')

@app.route('/')
def hello_world():
    data = {}
    mysql.query_db("select * from emails", data)
    return render_template('index.html', data = data)

@app.route('/validate', methods = ['POST'])
def index():
    addressToVerify = request.form['email']
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', request.form['email'])
    if match == None:
        flash('Email is not valid!')
        session['color'] = "red"
    else:
        query = "INSERT INTO emails (email, created_at, updated_at) VALUES(:email, NOW(), NOW())"
        data = {
            'email': addressToVerify
        }
        mysql.query_db(query, data)
        flash("The email address you entered " + addressToVerify + " is a VALID email address! Thank you!")
        session['color'] = "green"
        return redirect('/success')
    return redirect('/')
@app.route('/success')
def show():
    query = "SELECT id,email, created_at FROM emails"
    data = {}
    emails = mysql.query_db(query, data)
    print emails
    return render_template('success.html', emails=emails)

app.run(debug=True)

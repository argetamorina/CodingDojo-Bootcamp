from flask import Flask, render_template, request, redirect, flash, session
import re
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'secret'
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'mydb')

queries = {
    'select':'SELECT * FROM users',
    'insert':'INSERT INTO users (first_name,last_name,email,created_at,updated_at) VALUES(:first_name,:last_name,:email,NOW(),NOW())',
    'delete':'DELETE FROM users WHERE id=:id',
    'update':'UPDATE users SET first_name =:first_name, last_name=:last_name, email = :email, updated_at = NOW() WHERE id =:id',
    'show': "SELECT * FROM users WHERE id = :id"
}

@app.route('/')
def index():
    create = 2
    data = {}
    query = mysql.query_db(queries['select'], data)
    return render_template('index.html', query = query, create = create)

@app.route('/friends')
def create():
    create = 1
    return render_template('index.html', create = create)

@app.route('/create1', methods=['POST'])
def create1():
    addressToVerify = request.form['email']
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', request.form['email'])
    if match == None:
        flash('Email is not valid!')
    else:
        query = "INSERT INTO  users (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email']
        }
        mysql.query_db(query, data)
        return redirect('/friends')
    return redirect('/friends')

@app.route('/friends/<id>', methods=["POST"])
def update(id):
    query = queries['update']
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'id' :id
    }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<id>/edit', methods=["GET"])
def edit(id):
    query1 = queries['show']
    data = {
        'id': id
    }
    query = mysql.query_db(query1, data)[0]
    return render_template('create.html', query=query )

@app.route('/friends/<id>/delete', methods=["POST"])
def delete(id):
    query = queries['delete']
    data = {
        'id' : id
    }
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)

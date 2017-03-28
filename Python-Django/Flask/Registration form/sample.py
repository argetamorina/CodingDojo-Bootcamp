from flask import Flask, render_template, redirect, request
import re
app = Flask(__name__)

def hasNumbers(inputString):
    return bool(re.search(r'\d', inputString))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods = ['POST'])
def function():
    email_regex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
    data = request.form['name']
    if request.form['name'] == "" or request.form['last_name'] == "" or request.form['email'] == "" or request.form['password'] == "" or request.form['confirm_password'] == "":
        print 'Fill the form'
    if request.form['password'] !=request.form['confirm_password']:
        print "Your confirm password is wrong."
    elif len(request.form['password']) < 8:
        print 'Your password should be more than 8 characters'
    if not email_regex.match(request.form['email']):
        print 'Invalid Email'
    if hasNumbers(request.form['name']):
        print 'Name cannot contain any numbers'
    if hasNumbers(request.form['last_name']):
        print 'Last Name cannot contain any numbers'
    return redirect('/')
app.run(debug=True)

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('index.html')

# app.run(debug=True)

@app.route('/ninjas')
def ninjas1():
	return render_template('ninjas.html')

@app.route('/dojos/new')
def dojo():
	return render_template('dojos.html')
	
app.run(debug=True)
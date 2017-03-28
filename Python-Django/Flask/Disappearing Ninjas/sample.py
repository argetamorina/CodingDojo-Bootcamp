from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = 'very secret'
@app.route('/')
def index():
    session['no_ninja'] = 'No ninja here'
    return render_template('index.html')

@app.route('/ninjas')
def index2():
    session['photo'] = 1
    return render_template('index2.html')

@app.route('/ninjas/<ninjas_color>')
def function(ninjas_color):
    session['photo'] = 0
    ninjas = {
        'purple': 'donatello',
        'blue': 'leonardo',
        'orange': 'michelangelo',
        'red': 'raphael'
    }
    print ninjas
    if ninjas_color in ninjas:
        ninja = ninjas[ninjas_color]
        print ninja
    else:
        ninja = 'notapril'
        
    return render_template('index2.html', ninjas_color = ninja )
app.run(debug=True)

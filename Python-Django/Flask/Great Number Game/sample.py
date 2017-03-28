from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "very secret"

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/result', methods = ['POST'])
def create():
    try:
        data = request.form['name']
        input_num = int(data)
        # guessed_num = random.randrange(0, 101)
        guessed_num = 60
        session['show'] = ""
        session['playagain'] = 'hidden'
        print session['playagain']
        if input_num < guessed_num:
            session['show'] = 'Too Low'
            session['color'] = 'red'
        elif input_num > guessed_num:
            session['show'] = 'Too High'
            session['color'] = 'red'
        else:
            session['show'] = 'You guess the right number  '
            session['color'] = 'green'
            session['playagain'] = 'playagain'
        print data
        print 'hi'
    except:
        session['color'] = 'white'
        session['show'] = ""
        session['playagain'] = 'hidden'
        print data
    return redirect('/')

# @app.route('/create')
# def create2():

app.run(debug=True)

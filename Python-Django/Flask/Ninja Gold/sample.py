from flask import Flask, render_template, redirect, session, request
import random, datetime
app = Flask(__name__)
app.secret_key = "very secret"
now = datetime.datetime.now()

@app.route('/')
def index():
    try:
        session['total_point']
        session['action1']
    except:
        session['total_point'] = 0
        session['action1'] = []
    return render_template('index.html')

@app.route('/process_money', methods = ['POST'])

def function():
    value = request.form['building']
    session['action'] = ""
    session['color'] = 'green'

    if 'farm' == value:
        farm_point = int(random.randrange(10, 20))
        session['total_point'] += farm_point
        session['action'] = 'Earned %(first)d golds from the farm (' % {"first": farm_point}  + now.strftime("%Y-%m-%d %H:%M") + ')'
    elif 'cave' == value:
        cave_point = random.randrange(5, 10)
        session['total_point'] += cave_point
        session['action'] = 'Earned %(first)d golds from the cave (' % {"first": cave_point}  + now.strftime("%Y-%m-%d %H:%M") + ')'
        session['color'] = 'green'

    elif 'house' == value:
        house_point = random.randrange(2, 5)
        session['total_point'] += house_point
        session['action'] = 'Earned %(first)d golds from the house (' % {"first": house_point}  + now.strftime("%Y-%m-%d %H:%M") + ')'
    elif 'casino' == value:
        casino_point = random.randrange(-50, 50)
        session['total_point'] += casino_point
        if casino_point > 0:
            session['action'] = 'Entered a casino and win  %(first)d golds (' % {"first": casino_point}  + now.strftime("%Y-%m-%d %H:%M") + ')'
        else:
            session['action'] = 'Entered a casino and lost  %(first)d golds... Ouch (' % {"first": casino_point}  + now.strftime("%Y-%m-%d %H:%M") + ')'
            session['color'] = 'red'
    session['action1'].append(session['action'])
    print session['action1']
    return redirect('/')
app.run(debug=True)

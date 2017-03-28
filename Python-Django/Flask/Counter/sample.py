from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'very secret'


@app.route('/')
def counter():
    try:
        session['counter']
    except:
        session['counter'] = 0
    session['counter'] += 1
    return render_template('index.html')

@app.route('/add2', methods=['POST'])
def increment():
    print 'Hi'
    session['counter']+=1
    return redirect('/')

@app.route('/reset_count', methods=['POST'])
def reset():
    session['counter'] = 0
    return redirect('/')

if __name__ == "__main__":
    app.run()

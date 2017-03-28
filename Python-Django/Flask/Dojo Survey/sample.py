from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'very secret'

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/create', methods = ['POST'])
def create():
    data = request.form
    if request.form['name'] == "" or request.form['description'] == "":
        print 'Error'
    if len(request.form['description']) > 120:
        print 'To much characters'
    # print data
    return render_template('index1.html', data=data)
if __name__ == "__main__":
    app.run(debug=True)

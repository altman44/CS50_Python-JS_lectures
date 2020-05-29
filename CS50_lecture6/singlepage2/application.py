from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

texts = ["Content 1", "Content 2", "Content 3"]

@app.route('/first')
def first():
    return texts[0]

@app.route('/second')
def second():
    return texts[1]

@app.route('/third')
def third():
    return texts[2]


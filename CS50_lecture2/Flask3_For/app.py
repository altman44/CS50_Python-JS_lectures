# console: "export FLASK_APP=app"

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    names = ['Alice', 'Sophie', 'Max', 'Mary', 'Gandalph', 'Rupert', 'Rudolph']
    return render_template('index.html', names = names)


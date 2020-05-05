# console: "export FLASK_APP=app"

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello', methods=["GET","POST"])
def hello():
    if request.method == "GET":
        return "Please submit the form instead."
    else:
        name = request.form.get('name')
        return render_template('hello.html', name=name)

@app.route('/insert_data', methods=["POST"])
def insertar_datos():
    if request.form.get('fullname') == "" or request.form.get('age') == "":
        message = "At least one empty field"
    else:
        message = "Everything great"
    return message
# console: "export FLASK_APP=application.py" to allow that file be the main
# console: "flask run" (I must be inside the 'Flask' folder)
# console: "export FLASK_ENV=development" (debug mode: on) // it restarts the server when I change the file
# console: "FLASK_APP=application:app"

# creating a flask web server // Flask is going always to look the folder called 'templates' to render a template
from flask import Flask, render_template

# create a new web application // app is going to be the "source"
app = Flask(__name__)

# the function inmediately below "@app.route('/nameofroute')" is the one
# which is going to be executed
@app.route('/')
def index():
    return 'Hello, world!!!'

@app.route('/greet')
def welcome():
    return 'Welcome!'

@app.route('/greet/<string:name>')
def customizedWelcome(name):
    name = name.capitalize()
    return f'<h1>Welcome, {name}</h1>'

@app.route('/render_index')
def renderIndex():
    return render_template('index.html')

@app.route('/headline')
def renderIndexHeadline():
    headline = "Hello, I'm the headline"
    return render_template('index.html', headline=headline)

@app.route('/bye/<string:name>')
def bye(name):
    name = name.capitalize()
    return render_template('bye.html', name=name)

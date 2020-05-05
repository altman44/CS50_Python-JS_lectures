import requests

from flask import Flask, jsonify, render_template, request

# initializing Flask app with static files
app = Flask(__name__)

@app.route('/')
def index():
    res = requests.get('http://localhost:3000/api')
    data = res.json()['info']
    return render_template('index.html', data=data)

@app.route('/getDataFromBook', methods=['POST'])
def getDataFromBook():
    print('APP.PY')
    # Query for data from localhost:3000 (see API folder)
    res = requests.get('http://localhost:3000/api')

    # Make sure request succeeded
    if res.status_code != 200:
        return jsonify({"success": False, "error": 'Error. Status code: {res.status_code}'})
    
    # Make sure id is in response
    data = res.json()
    
    try:
        id = int(request.form.get('id_book'))
    except ValueError:
        return jsonify({"success": False, "error": 'Incorrect id value'})

    for book in data['info']:
        if book['id'] == id:
            return jsonify({"success": True, "book": book})

    return jsonify({"success": False, "error": 'ID not found'})


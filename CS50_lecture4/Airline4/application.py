from flask import Flask, render_template, request
from models import *
from classes import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://me:toto2222@localhost:5432/cs50'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# GENERAL FUNCTIONS
def validFlightFields(origin, destination, duration):
    if origin is None or destination is None or duration is None:
        return ValidationFlightFields(error = True, type = 'danger', message = 'You must fill in all the fields!')
    try:
        duration = int(duration)
    except ValueError:
        return ValidationFlightFields(error = True, type = 'danger', message = 'Duration must be an integer number')

    return ValidationFlightFields(error = False, type = None, message = None)

# ROUTES
# Main
@app.route('/')
def index():
    flights = Flight.query.all()
    flight = Flight.query.get(1)
    return render_template('index.html', flights=flights)

# Books
@app.route('/book', methods=["POST"])
def book():
    """Book a flight."""

    # Get form information
    name = request.form.get('name')
    if name == '':
        return render_template('index.html', type = 'danger', message = 'You must enter the passenger name!')
    try:
        flight_id = int(request.form.get('flight_id'))
    except ValueError:
        return render_template('index.html', type = 'danger', message = 'Invalid flight number!')
        
    # Make sure the flight exists
    flight = Flight.query.get(flight_id)
    if not flight:
        return render_template('index.html', type = "danger", message = 'No such flight with that id!')
    
    # Add passenger
    flight.add_passenger(name)
    return render_template('index.html', type = 'success', message = 'Registration done successfully!')

# Flights
@app.route('/flights')
def flights():
    """List all flights."""
    flights = Flight.query.all()
    name='Bob'
    flight = Passenger.query.filter_by(name=name).first().flight
    return render_template('flights.html', flights=flights, name=name, flight=flight)

@app.route('/flights/<int:flight_id>')
def flight(flight_id):
    """List details about a single flight."""

    # Make sure flight exists.
    flight = Flight.query.get(flight_id)
    if flight is None:
        return render_template('flights.html', type="danger", message="No such flight")

    # Get all passengers.
    passengers = flight.passengers
    return render_template('flight.html', flight=flight, passengers=passengers)

# Additions
@app.route('/add_flights')
def addFlights():
    return render_template('add_flights.html')

@app.route('/add_flight', methods=["POST"])
def addFlight():
    """Add a flight."""
    
    # Get form information
    origin = request.form.get('origin')
    destination = request.form.get('destination')
    duration = request.form.get('duration')

    # Make sure all fields are valid
    validation = validFlightFields(origin, destination, duration)
    if validation.error == True:
        return render_template('add_flights.html', type = validation.type, message = validation.message)
    
    flight = Flight(origin=origin, destination=destination, duration=duration)
    db.session.add(flight)
    db.session.commit()
    return render_template('add_flights.html', type = 'success', message = f'Added a flight from {origin} to {destination} with a duration of {duration} minutes')    

# Updates
@app.route('/update_flights')
def updateFlights():
    flights = Flight.query.all()
    return render_template('update_flights.html', flights=flights)

@app.route('/load_data_flight', methods=["POST"])
def loadDataFlight():
    try:
        id = int(request.form.get('id'))
    except ValueError:
        return render_template('update_flights.html', type = 'danger', message = 'No such flight id')
    
    flights = Flight.query.all()
    dataFlight = Flight.query.get(id)
    
    if dataFlight is None:
        return render_template('update_flights.html', type = 'danger', message = 'No such flight id')
    return render_template('update_flights.html', flights=flights, dataFlight = dataFlight, selectedID = id)

@app.route('/update_flight')
def updateFlight():
    """Update a flight."""
    
    # Get form information
    origin = request.form.get('origin')
    destination = request.form.get('destination')
    duration = request.form.get('duration')

    # Make sure all fields are valid
    validation = validFlightFields(origin, destination, duration)
    if validation.error == True:
        return render_template('update_flights.html', type = validation.type, message = validation.message)
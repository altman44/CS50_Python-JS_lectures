# it is the same that list.py but with Flight.query.all() instead of the "SELECT ... FROM flights"

from flask import Flask, render_template, request
# "import *": import everything, import all the classes (and I suppose functions too)
from models import *
from sqlalchemy import and_, or_

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://me:toto2222@localhost:5432/cs50"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# "db.init_app(app)": tie this database with this flask application
db.init_app(app)

def filterPassengers_byID(id):
    passengers = Passenger.query.filter_by(flight_id=id).all()
    counter = 1
    print("With the 'FILTER_BY' command:")
    for passenger in passengers:
        print(f"Passenger Num.{counter}: {passenger.name}")
        counter += 1
    
    if counter == 1:
        print("No passengers")

def joinByIDs(id):
    result = db.session.query(Flight, Passenger).filter(Flight.id == Passenger.flight_id).all()
    print("With the 'JOIN' command:")
    thereArePassengers = False
    for table in result:
        if id == table[0].id and id == table[1].flight_id:
            print(f"Name: {table[1].name}")
            thereArePassengers = True
    if thereArePassengers == False:
        print("No passengers")

def getOriginCount(origen):
    count = Flight.query.filter_by(origin=origen).count()
    return count

def deleteFlight():
    answer = input("Would you like to delete a flight?('Yes' to delete) : ")
    if answer == "Yes" or answer == "Y":
        flightID_Delete = int(input("Which flight are you going to delete (ID): "))
        flightToDelete = Flight.query.get(flightID_Delete)
        db.session.delete(flightToDelete)
        db.session.commit()

def orderBy():
    print("Order by name of every passenger in an ascending way:")
    print(Passenger.query.order_by(Passenger.name).all())
    print("Order by name of every passenger in a descending way:")
    print(Passenger.query.order_by(Passenger.name.desc()).all())

def showNamesOut():
    namesOut = ['Joe', 'Nico', 'Marcelo', 'Luca', 'Amy']
    print(f"Passengers who aren't {namesOut}")
    
    passengers = Passenger.query.all()
    for passenger in passengers:
        ok = True
        for nameOut in namesOut:
            if passenger.name == nameOut:
                ok = False   
        if ok:
            print(passenger.name)

def showOriginsWithLetter():
    letter = input("Enter a letter: ")
    print(f"Origins with the letter '{letter}':")
    flights = Flight.query.filter(Flight.origin.like(f"%{letter}%")).all()
    for flight in flights:
        print(flight.origin)

def showOriginsIN(origins):
    # NOT IN: ~Flight.origin.in_([])
    flights = Flight.query.filter(Flight.origin.in_(origins)).all()
    print(f"Destinations of the origins {origins}: ")
    for flight in flights:
        print(f"ID({flight.id}). Destination of {flight.origin}: {flight.destination}")

def showDestinationAndDuration(destination, greaterThan):
    flights = Flight.query.filter(and_(Flight.destination == destination, Flight.duration > greaterThan)).all()
    print(f"{destination} destinations that last longer than {greaterThan}")
    for flight in flights:
        print(f"Duration: {flight.duration}")

def showDestinationOrDuration(destination, greaterThan):
    flights = Flight.query.filter(or_(Flight.destination == destination, Flight.duration > greaterThan)).all()
    print(f"Flights with {destination} as destination or that last longer than {greaterThan}")
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes")

def main():
    # flights is going to be a list. Each element is an individual flight
    flights = Flight.query.all()
    for flight in flights:
        
        # flight.duration += 10

        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes")
        
        # One way
        filterPassengers_byID(flight.id)
        # Another way
        joinByIDs(flight.id)
        
        count = getOriginCount(flight.origin)
        if count == 1:
            print(f"This origin is repeated {count} time")
        else:
            print(f"This origin is repeated {count} times")
        
        print(f"{Flight.query.get(flight.id)}") # it return an object that represents the row in the table
        
        print()
    db.session.commit()
    
    deleteFlight()
    print()
    orderBy()
    print()
    showNamesOut()
    print()
    showOriginsWithLetter()
    print()
    showOriginsIN(['Tokyo', 'Paris', 'London'])
    print()
    showDestinationAndDuration('New York', 1110)
    print()
    showDestinationOrDuration('New York', 1110)
    

if __name__ == "__main__":
    with app.app_context():
        main()
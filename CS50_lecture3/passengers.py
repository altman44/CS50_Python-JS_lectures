import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql://me:toto2222@localhost:5432/cs50")
db = scoped_session(sessionmaker(bind=engine))

def main():
    # List all flights
    flights = db.execute("SELECT id, origin, destination, duration FROM flights").fetchall()
    for flight in flights:
        print(f"Flight {flight.id}: {flight.origin} to {flight.destination}, {flight.duration} minutes")

    # Promt user to choose a flight
    flight_id = int(input("\nFlight ID: "))
    flight = db.execute("SELECT origin, destination, duration FROM flights WHERE id = :id",
                        {"id": flight_id}).fetchone()
    
    # Make sure flight is valid
    if flight is None:
        print("Error: No such flight.")
        return
    
    # List passengers
    passengers = db.execute("SELECT name FROM passengers WHERE flight_id = :flight_id",
                            {"flight_id": flight_id}).fetchall()
    
    print("\nPassengers:")
    counter = 0
    for passenger in passengers:
        counter = counter + 1
        print(f"{counter}: {passenger.name}")
    if len(passengers) == 0:
        print("No passengers.")
    else:
        print(f"Total de pasajeros: {len(passengers)}")

if __name__ == "__main__":
    main()
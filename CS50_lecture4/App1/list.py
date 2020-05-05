from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql://me:toto2222@localhost:5432/cs50")
db = scoped_session(sessionmaker(bind=engine))

def main():
    flights = db.execute("SELECT origin, destination, duration FROM flights")
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes")

if __name__ == "__main__":
    main()
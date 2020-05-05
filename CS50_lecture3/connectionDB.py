# selecting data

# console: pip install SQLAlchemy  # to install sqlalchemy
# console: pip install psycopg2-binary  # it did not recognize psycopg2 module so I had to do this

# importing an operating system library
import os

# sqlalchemy is a library
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# creating a database engine. The engine is an object created by sqlaclchemy that manage the connections with databases
# engine = create_engine(os.getenv("DATABASE_URL"))
# engine = create_engine(os.getenv("postgresql:///cs50"))
# engine = create_engine("postgresql://username:password@localhost:5432/name_db")
engine = create_engine("postgresql://me:toto2222@localhost:5432/cs50")

# "scoped_session" separate between all the people that is using my web page. Create different sessions
db = scoped_session(sessionmaker(bind=engine))

def main():
    flights = db.execute("SELECT origin, destination, duration FROM flights").fetchall()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")

if __name__ == "__main__":
    main()


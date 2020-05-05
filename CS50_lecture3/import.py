# Read the flights.csv (import it) file and insert data

import csv
# import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql://me:toto2222@localhost:5432/cs50")
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("flights.csv")
    reader = csv.reader(f)
    for origen, destino, duracion in reader:
        db.execute("INSERT INTO flights (origin, destination, duration) VALUES (:origin, :destination, :duration)", 
                    {"origin": origen, "destination": destino, "duration": duracion})
        print(f"Added flight from {origen} to {destino}, {duracion}")
    db.commit()

if __name__ == "__main__":
    main()
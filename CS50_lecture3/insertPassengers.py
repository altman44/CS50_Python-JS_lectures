import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql://me:toto2222@localhost:5432/cs50")
db = scoped_session(sessionmaker(bind=engine))

def main():
    ins = open("passengers.csv")
    reader = csv.reader(ins)
    for name, flight_id in reader:
        db.execute("INSERT INTO passengers (name, flight_id) VALUES (:name, :flight_id)",
                    {"name": name, "flight_id": flight_id})
        print(f"Added {name} to Flight ID: {flight_id}")
    db.commit()

if __name__ == "__main__":
    main()
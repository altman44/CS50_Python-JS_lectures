from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Every table from the database represents one class
# "db.model": the class is inheriting from db.Model or the model of SQLAlchemy

class Flight(db.Model):
    __tablename__ = "flights"
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String, nullable=False)
    destination = db.Column(db.String, nullable=False)
    duration = db.Column(db.Integer, nullable=False)

class Passenger(db.Model):
    __tablename__ = "passengers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    flight_id = db.Column(db.Integer,db.ForeignKey("flights.id"), nullable=False)

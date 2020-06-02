from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id} - {self.origin} to {self.destination}"

class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"

# Comments
# CREATE ROW
# "f = Flight(origin="Buenos Aires", destination="London", duration=100)"
# "f.save()"
# QUERIES
# "Flight.objects.all()" # returns a QuerySet so...
# ... I added de "__str__" function which return a QuerySet but as String Format
# "f = Flight.objects.first()"
# "f.origin" # Like a dictionary I think
# "f.delete()" delete that row
# 
# Now it has changed adding Airport class as well as the ForeignKey in Flight class
#  jfk = Airport(code="JFK", city="New York City")
# lhr = Airport(code="LHR", city="London")
# jfk.save()
# lhr.save()
# f = Flight(origin=jsfk, destination=lhr, duration=415)
# f.save()
# f.origin.city # it returns "New York City"
# jfk.departures.all() # it returns all the departures from JFK
# Added Passenger class
# To create the table and the in-between table for the Passengers
# "python manage.py sqlmigrate flights 0003"
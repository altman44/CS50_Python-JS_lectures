from django.contrib import admin
from .models import Airport, Flight, Passenger

# Register your models here.
admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(Passenger)

# Registering these models in order to update them later
# The admin site is able to manipulate those classes
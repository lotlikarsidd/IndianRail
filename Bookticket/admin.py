from django.contrib import admin
from .models import Time, Routes, Trains, Tickets, Customer, Passenger, Schedule

# Register your models here.


admin.site.register(Routes)

admin.site.register(Time)

admin.site.register(Trains)

admin.site.register(Customer)

admin.site.register(Passenger)

admin.site.register(Tickets)

admin.site.register(Schedule)

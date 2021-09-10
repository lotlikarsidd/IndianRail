from django.db import models
# Create your models here.



class Time(models.Model):
    Time_id = models.IntegerField(primary_key=True)
    Arrival_Time = models.CharField(max_length=5)
    Departure_Time = models.CharField(max_length=5)


class Routes(models.Model):
    Route_id = models.CharField(primary_key=True, max_length=4)
    source = models.CharField(max_length=30)
    destination = models.CharField(max_length=30)
    fare = models.CharField(max_length=30)


class Trains(models.Model):
    Train_id = models.CharField(primary_key=True, max_length=50)
    Train_name = models.CharField(max_length=30)
    Route_id = models.ForeignKey(Routes, on_delete=models.CASCADE)
    Time_id = models.ForeignKey(Time, on_delete=models.CASCADE)


class Tickets(models.Model):
    Ticket_id = models.IntegerField(primary_key=True)
    Train_id = models.ForeignKey(Trains, on_delete=models.CASCADE)
    Compartment_no = models.CharField(max_length=5)
    Berth_type = models.CharField(max_length=10)
    Seat_No = models.IntegerField()


class Customer(models.Model):
    Email = models.EmailField(primary_key=True)
    Name = models.CharField(max_length=50)
    Age = models.IntegerField()
    Time_of_registration = models.DateTimeField(auto_now_add=True)
    Phone = models.CharField(max_length=13)
    Password = models.CharField(max_length=500)


class Passenger(models.Model):
    P_id = models.AutoField(primary_key=True)
    Email = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    Age = models.IntegerField()
    Dare_of_booking = models.DateTimeField(auto_now_add=True)
    On_boarding_Date = models.DateField()
    Aadhar = models.CharField(max_length=12)
    Phone = models.CharField(max_length=33)
    Gender = models.CharField(max_length=20)
    Ticket_id = models.ForeignKey(Tickets, on_delete=models.CASCADE)


class Schedule(models.Model):
    date = models.DateField()
    Train_id = models.ForeignKey(Trains, on_delete=models.CASCADE)

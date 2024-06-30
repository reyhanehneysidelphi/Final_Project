from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    date = models.DateField()
    organizer_email = models.EmailField()

    def __str__(self):
        return self.title

class TicketSale(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()

class ManageAttendees(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    message = models.TextField()

class ManagersPlanner(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    to_do_list = models.TextField()
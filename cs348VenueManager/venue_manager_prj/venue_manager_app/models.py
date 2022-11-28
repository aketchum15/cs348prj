from django.db import models
from django.db.models.query import django

# Create your models here.
class HomePage(models.Model):
    date = models.DateField()
    performer = models.CharField(max_length=100)
    venue = models.CharField(max_length=100)
    ticket_price = models.IntegerField(default=0)

class Performers(models.Model):
    name = models.CharField(max_length=100)
    num_crew_memeber = models.IntegerField(default=0)
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Owners(models.Model):
    name = models.CharField(max_length=100)
    num_venues = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Venues(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(Owners, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Shows(models.Model):
    num_attendees = models.IntegerField(default=0)
    performer = models.ForeignKey(Performers, on_delete=models.CASCADE)
    ticket_price = models.IntegerField(default=0)
    venue = models.ForeignKey(Venues, on_delete=models.CASCADE)
    date = models.DateField(default=django.utils.timezone.now)

class Attendees(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField(default=0)
    card_number = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Tickets(models.Model):
    show = models.ForeignKey(Shows, on_delete=models.CASCADE)
    attendee = models.ForeignKey(Attendees, on_delete=models.CASCADE)

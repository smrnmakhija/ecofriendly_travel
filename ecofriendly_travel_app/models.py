from django.db import models

# Create your models here.


class User(models.Model):
    email = models.CharField(max_length=200, primary_key=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    carbon_footprint = models.FloatField()
    total_eco_points = models.FloatField()
    phone = models.IntegerField(max_length=10)


class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    distance = models.FloatField()
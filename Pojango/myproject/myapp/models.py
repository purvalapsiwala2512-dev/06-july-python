from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=20)
    qty=models.IntegerField
    Tkt_price=models.FloatField

class Mobile(models.Model):
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=30)
    price = models.FloatField

class Restaurant(models.Model):
    name = models.CharField(max_length=40)
    dish = models.CharField(max_length=30)
    rating = models.IntegerField       
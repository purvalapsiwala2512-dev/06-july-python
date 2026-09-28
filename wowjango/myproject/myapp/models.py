from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    price = models.FloatField()

class Car(models.Model):
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    price = models.FloatField()    
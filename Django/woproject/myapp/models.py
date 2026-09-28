from django.db import models

# Create your models here.
class Travel(models.Model):
    country = models.CharField(max_length=30)
    days = models.IntegerField()
    cost = models.FloatField()
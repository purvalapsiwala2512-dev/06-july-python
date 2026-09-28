from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50)
    duration = models.IntegerField()
    fees = models.FloatField()
    

class Teacher(models.Model):
    name = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    experience = models.IntegerField()
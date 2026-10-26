from django.db import models
# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=20)

class Capital(models.Model):
    country = models.OneToOneField(Country,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    # def __str__(self):
    #     return self.name
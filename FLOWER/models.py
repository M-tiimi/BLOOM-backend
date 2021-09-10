from django.db import models

# Create your models here.

class Flower(models.Model):
    color = models.CharField(max_length=50)
    wellness = models.CharField(max_length=100)

    def __str__(self):
        return 'I am '+self.color+' Flower'
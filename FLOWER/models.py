from django.db import models

# Create your models here.

class Flower(models.Model):
    color = models.CharField(max_length=50)
    wellness = models.CharField(max_length=100)

    
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# Create your models here.
# An id field is added automatically, but this behavior can be overridden
class User(AbstractBaseUser):
    username = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

class Flower(models.Model):
    color = models.CharField(max_length=50)
    wellness = models.CharField(max_length=100)
    points = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'I am '+self.color+' Flower'

class Question(models.Model):
    title = models.CharField(max_length=40)

class Answer(models.Model):
    title = models.CharField(max_length=1000)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

class Task(models.Model):
    points = models.ForeignKey(Flower, on_delete=models.CASCADE)
    user = user = models.ForeignKey(User, on_delete=models.CASCADE)

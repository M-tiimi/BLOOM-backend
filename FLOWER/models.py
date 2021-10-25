from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# models created here
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
    user = models.OneToOneField('User', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return 'I am '+self.color+' Flower'

class Question(models.Model):
    title = models.CharField(max_length=40)
   

class Answer(models.Model):
    title = models.CharField(max_length=1000)
    

class Task(models.Model):
    points = models.IntegerField()
    

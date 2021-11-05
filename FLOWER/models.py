from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# This file is for creating models that are saved as database tables

# An id field is added automatically, but this behavior can be overridden
class User(AbstractBaseUser):
    username = models.CharField(max_length=20)
    birth_year = models.IntegerField()
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
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name="flower") 

    def __str__(self):
        return 'I am '+self.color+' Flower'

class Question(models.Model):
    title = models.CharField(max_length=40)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="question")
   

class Answer(models.Model):
    title = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, related_name= "answer")
    

class Task(models.Model):
    points = models.IntegerField()
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE, null=True, related_name='task')
    

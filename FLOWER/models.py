from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)


# This file is for creating models that are saved as database tables
class UserManager(BaseUserManager):
    def create_user(self, username, birth_year, email, password=None):
        """
        Creates and saves a User
        """
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            username=username,
            birth_year=birth_year,
            email = self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, birth_year, password=None):
        """
        Creates and saves a superuser 
        """
        user = self.create_user(
            username= username,
            birth_year=birth_year,
            email = self.normalize_email(email)
        )

        user.is_admin = True
        user.save(using=self._db)
        return user



# An id field is added automatically, but this behavior can be overridden
class User(AbstractBaseUser):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=200)
    birth_year = models.IntegerField()
    points = models.IntegerField(null =True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['password', 'email', 'birth_year']

    USERNAME_FIELD = 'username'
    objects = UserManager()


    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin    

    def __str__(self):
        return self.username



class Question(models.Model):
    title = models.CharField(max_length=40)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="question")
   

class Answer(models.Model):
    title = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, related_name= "answer")
    

class Task(models.Model):
    title = models.CharField(max_length=1000, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='task')
    

class Try(models.Model):
    title = models.CharField(max_length=40)
     

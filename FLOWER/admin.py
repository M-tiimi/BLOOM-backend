from django.contrib import admin
from django.contrib.auth.models import Group
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
from .models import Answer, Question, Task, User, UserManager



admin.site.register(User)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Task)

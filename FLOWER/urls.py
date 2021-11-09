from django.http import request
from django.urls import path
from . import views
from django.shortcuts import render

#urls for views, check BLOOMbackend folder where urls.py is
urlpatterns = [
    path('', views.FlowerList.as_view()),
    path('users/', views.UserList.as_view()),
    path('questions/', views.QuestionList.as_view()),
    path('answers/', views.AnswerList.as_view()),
    path('ml-model/', views.call_model.as_view()),
    
    
]
from django.http import request
from django.urls import path
from . import views
from django.shortcuts import render

#urls for views, check BLOOMbackend folder where urls.py is
urlpatterns = [
    path('', views.UserList.as_view()),
    path('questions/', views.QuestionList.as_view()),
    path('answers/', views.AnswerList.as_view()),
    path('ml-model/', views.call_model),
    path('current_user/', views.current_user),
    
    
]
from django.http import request
from django.urls import path
from . import views
from django.shortcuts import render

#urls for views, check BLOOMbackend folder where urls.py is
urlpatterns = [
    path('', views.UserList.as_view()),
    path('ml-model/', views.call_model),
    path('current_user/', views.current_user),
    path('task/<int:pk>', views.get_task_by_id),
    path('question/<int:pk>', views.get_question_by_id),
    path('tasks/', views.TaskList.as_view()),
    path('usertasks/<int:pk>', views.get_user_tasks)

]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.flower_list),
    path('flowers/', views.flower_list),
    path('users/', views.UserList.as_view()),
    path('questions/', views.QuestionList.as_view()),
    path('answers/', views.AnswerList.as_view()),
]
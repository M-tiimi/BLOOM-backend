from django.urls import path
from . import views

urlpatterns = [
    path('', views.flower_list),
    path('flowers/', views.flower_list),
    path('users/', views.UserList.as_view()),
]
from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.apitest, name='apitest'),
    path('flowers/', views.flower_list),
]
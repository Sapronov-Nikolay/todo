from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
]
# Создали локально новый urls.py для приложения tasklist
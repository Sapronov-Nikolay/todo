from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add', views.add_task)
]
# Создали локально новый urls.py для приложения tasklist
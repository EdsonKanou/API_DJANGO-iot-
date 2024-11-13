from django.contrib import admin
from django.urls import path
from API_IOT import views

urlpatterns = [
    path("iot/",views.list, name='home' ),
]

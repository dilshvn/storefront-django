from django.urls import path
from . import views

#this is an url configuration module
urlpatterns = [
    path('hello/', views.say_hello)
]
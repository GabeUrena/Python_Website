from django.urls import path
from . import views #from the current folder import the views module


urlpatterns = [
    path("", views.index),
    path("new", views.new)
]

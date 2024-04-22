from django.db import models

# Create your models here.
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]

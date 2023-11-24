from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path("create",createUserView.as_view(), name="create"),
]

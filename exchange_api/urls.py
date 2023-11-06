from django.urls import path
from . import views

urlpatterns = [
    path("currency/", views.exchangeApi, name="home"),
]

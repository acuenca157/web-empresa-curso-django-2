from django.urls import path
from . import views

urlpatterns = [
    #Paths from contact
    path('', views.contact, name="contact"),
]
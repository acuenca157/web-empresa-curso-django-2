from django.urls import path
from . import views

urlpatterns = [
    #Paths from core
    path('services/', views.services, name="services"),
]
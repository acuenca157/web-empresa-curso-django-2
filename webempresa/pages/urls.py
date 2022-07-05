from django.urls import path
from . import views

urlpatterns = [
    #Paths from core
    path('<int:page_id>/<slug:page_slug>', views.page, name="page")
]
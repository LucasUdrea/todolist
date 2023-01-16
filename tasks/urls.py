from django.urls import path   
from . import views

# This will reroute all our urls for using them in our app

urlpatterns = [
    path ("", views.index, name= "index"),
]
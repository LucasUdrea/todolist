from django.urls import path   
from . import views

# This will reroute all our urls for using them in our app
app_name = "tasks"
urlpatterns = [
    path("", views.index, name= "index"),
    path("add", views.add, name="add")
]
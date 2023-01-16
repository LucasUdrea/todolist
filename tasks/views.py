from django.shortcuts import render
# List of tasks to do
tasks = ["foo", "bar", "Jeez"]
# Create your views here.

def index (request) :
    # We add a context variable using a dictionary telling django 
    # That we want to use the task list in the index.html 
    return render (request, "tasks/index.html", { "tasks" : tasks
    })
from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.

# Views are not really what a regular developer would think
# In python they act more like request handelers
# What we would call a view in react in python is called a template

def homepage(request):
    #return HttpResponse("Hello World")
    return render(request,'home.html')


def about(request):
    #return HttpResponse("about")
    return render(request,'about.html')

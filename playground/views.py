from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.

# Views are not really what a regular developer would think
# In python they act more like request handelers
# What we would call a view in react in python is called a template

def say_hello(request):
    return render(request, 'hello.html',{"name":"liquen"})



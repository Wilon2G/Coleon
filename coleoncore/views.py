from django.shortcuts import render

# Create your views here.

def my_collections(request):
    return render(request, 'my_collections.html')

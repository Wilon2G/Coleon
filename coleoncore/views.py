from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from coleoncore.models import Coleoncore, Article, Name, Image, Status  # Collection model :)
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from django.apps import apps
from coleoncore.utils.CollectionHandler import CollectionHandler  #CollectionHandler is the class that represents and manages the collections (a lot)
from django.http import JsonResponse



#Shows the collections of a user, also creates new collections
@login_required(login_url="/users/login/")
def my_collections(request):
    user = request.user
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            # This calls the CollectionHandler class to create a new collection
            CollectionHandler.create_collection(user,title)
            #print("==============================================")
            #print(c)
            return redirect("/collections/my_collections/")  
    collections = Coleoncore.objects.filter(user=user).order_by("-created_at") #Gets the collections of the user and orders by creation date
    return render(request, 'my_collections.html', {
        "collections": collections,
        "name": user.first_name or user.username, 
    })



#DELETES a collection
@require_POST
@login_required(login_url="/users/login/")
def delete_collection(request, collection_id):
    collection = get_object_or_404(Coleoncore, id=collection_id, user=request.user)
    collection.delete()
    return redirect("/collections/my_collections/")



#Visualizes a collection
@login_required(login_url="/users/login/")
def update_collection(request, collection_id):
    collection = get_object_or_404(Coleoncore, id=collection_id, user=request.user)
    if request.method == "POST":
        new_article=CollectionHandler.new_article(collection)
        #print("================================")
        #print(new_article)
        return JsonResponse({"status": "success","new_article":new_article}) 

    handler=CollectionHandler(collection)

    #print(handler.articles)
    return render(request, 'collection_update.html', {
        "collection": handler,
    })

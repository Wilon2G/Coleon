from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from coleoncore.models import Coleoncore, Article, Name, Image, Status  # Collection model :)
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from django.apps import apps
from .utils import CollectionHandler  #CollectionHandler is the class that represents and manages the collections (a lot)



#Shows the collections of a user, also creates new collections
@login_required(login_url="/users/login/")
def my_collections(request):
    user = request.user
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            # This calls the CollectionHandler class to create a new collection
            CollectionHandler.create_collection(user=user, title=title)
            return redirect("/collections/my_collections/")  

    collections = Coleoncore.objects.filter(user=user).order_by("-created_at") #Gets the collections of the user and orders by creation date

    return render(request, 'my_collections.html', {
        "collections": collections,
        "name": user.first_name or user.username, 
    })




@require_POST
@login_required(login_url="/users/login/")
def delete_collection(request, collection_id):
    collection = get_object_or_404(Coleoncore, id=collection_id, user=request.user)
    collection.delete()
    return redirect("/collections/my_collections/")



# A lot going on here, but its kinda like a reverse search for an article and returns an associative array with all the information
def get_article_related_data(article):
    related_data = {}
    for field in article._meta.get_fields():
        if field.is_relation and field.one_to_many and field.auto_created:
            related_name = field.get_accessor_name()
            related_manager = getattr(article, related_name)

            if related_manager.exists():
                model_name = field.related_model.__name__.lower()
                related_instance = related_manager.first()

                if hasattr(related_instance, 'value'):
                    value = related_instance.value

                    # If there are more fields, include them as a sub-array
                    other_fields = {
                        f.name: getattr(related_instance, f.name)
                        for f in related_instance._meta.fields
                        if f.name != 'id' and f.name != 'article_id' and f.name != 'value'
                    }

                    if other_fields:
                        related_data[model_name] = {"value": value, **other_fields}
                    else:
                        related_data[model_name] = value
                else:
                    related_data[model_name] = str(related_instance)  # fallback
    return related_data



@login_required(login_url="/users/login/")
def update_collection(request, collection_id):
    collection = get_object_or_404(Coleoncore, id=collection_id, user=request.user)
    articles = collection.articles.all().order_by("created_at")
    rows=[]
    for article in articles:
        rows.append(get_article_related_data(article))
    
    print(rows)

    return render(request, 'collection_update.html', {
        "collection": collection,
        "rows":rows,

    })

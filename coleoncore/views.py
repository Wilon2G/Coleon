from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from coleoncore.models import Coleoncore  # update this if your model is elsewhere

@login_required(login_url="/users/login/")
def my_collections(request):
    user = request.user

    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            Coleoncore.objects.create(user=user, title=title)
            return redirect("/collections/my_collections/")  

    collections = Coleoncore.objects.filter(user=user).order_by("-created_at")

    return render(request, 'my_collections.html', {
        "collections": collections,
        "name": user.first_name or user.username, 
    })

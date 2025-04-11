from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, logout_required #Interesting wraper made by me, it ensures a logged user does not access a place it should not

# Create your views here.
@logout_required(login_url="/")
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save()) #Form.save returns the user so can be used to login directly after register
            return redirect("/")
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", {"form":form})

@logout_required(login_url="/")
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #LOGIN HERE
            login(request, form.get_user())
            #This logic controls that if the user is redirected from a login-restircted page, when it logs in it will be redirected to that restricted page instead of the default one
            if "next" in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect("/")
    else:
        form=AuthenticationForm()
    
    return render(request, "users/login.html", {"form":form})

@login_required(login_url="/users/login/")
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")
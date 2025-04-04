from django.urls import path
from . import views

# App to control the users
app_name = 'users'

urlpatterns = [
    path('register/', views.register_view, name="register")
]

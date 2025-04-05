from django.urls import path
from . import views

app_name="playground"
# URL Conf
urlpatterns=[
    path('hello/', views.say_hello),
    path('kk/', views.kk)

]
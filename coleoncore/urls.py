from django.urls import path
from . import views

app_name="coleoncore"
# URL Conf
urlpatterns=[
    path('my_collections/', views.my_collections),

]
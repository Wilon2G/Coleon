from django.urls import path
from . import views

app_name = 'collections'

urlpatterns = [
    path('my_collections/', views.my_collections, name="my_collections"),
    path('my_collections/delete/<int:collection_id>', views.delete_collection, name="delete"),

]
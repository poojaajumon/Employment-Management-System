from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.home),
    path('index',views.index),
    path('about',views.add),
    path('insert',views.insert),
    path('delete/<id>',views.delete),
    path('edit/<id>',views.edit),
    
]

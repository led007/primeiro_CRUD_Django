# meu_projeto/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    
    path('', include('produtos.urls')),
   
]

from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('genre/<str:slug>/', genre_detail, name='genre'),
    path('recipe-detail/<int:pk>/', recipe_detail, name='detail'),
]
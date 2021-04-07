from django.urls import path

from .views import *

urlpatterns = [
    path('', MainPageView.as_view(), name='home'),
    path('genre/<str:slug>/', GenreDetailView.as_view(), name='genre'),
    path('recipe-detail/<int:pk>/', RecipeDetailView.as_view(), name='detail'),
    path('add-recipe/', add_recipe, name='add-recipe'),
    path('update-recipe/<int:pk>/', update_recipe, name='update-recipe'),
    path('delete-recipe/<int:pk>/', DeleteRecipeView.as_view(), name='delete-recipe'),
]
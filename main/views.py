from django.shortcuts import render, get_object_or_404

# Create your views here.
from main.models import *


def index(request):
    return render(request, 'index.html')

def genre_detail(request, slug):
    genre = Genre.objects.get(slug=slug)
    recipes = Recipe.objects.filter(genre_id=slug)
    return render(request, 'category-detail.html', locals())


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    image = recipe.get_image
    images = recipe.images.exclude(id=image.id)
    return render(request, 'recipe-detail.html', locals())



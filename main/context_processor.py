from .models import Genre

def get_genre(request):
    genres = Genre.objects.filter(parent__isnull=True)
    return {'genres': genres}
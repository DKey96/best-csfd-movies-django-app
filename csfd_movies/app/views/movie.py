from app.models import Movie
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render


def movie_detail(request, movie_id: int) -> HttpResponse:
    movie_model = get_object_or_404(Movie, id=movie_id)
    return render(request, "movie.html", {"movie": movie_model})

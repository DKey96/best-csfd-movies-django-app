from app.models import Actor, Movie
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render


def search(request) -> HttpResponse:
    query = request.GET.get("q")
    movies = (
        Movie.objects.filter(Q(title__icontains=query)).distinct() if query else []
    )
    actors = Actor.objects.filter(name__icontains=query) if query else []

    context = {"query": query or "", "movies": movies or [], "actors": actors or []}

    return render(request, "search.html", context)

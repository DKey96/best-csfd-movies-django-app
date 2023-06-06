from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from app.lib.string_normalization import strip_accents
from app.models import Movie, Actor


def search(request) -> HttpResponse:
    query = request.GET.get("q") or ""
    query_normalized = strip_accents(query)
    movies = Movie.objects.filter(Q(title_normalized__icontains=query_normalized)) if query else []
    actors = Actor.objects.filter(Q(name_normalized__icontains=query_normalized)) if query else []

    context = {"query": query or "", "movies": movies or [], "actors": actors or []}

    return render(request, "search.html", context)

from app.views import actor, movie, search
from django.urls import path

urlpatterns = [
    path("", search.search, name="search"),
    path("movies/<int:movie_id>/", movie.movie_detail, name="movie_detail"),
    path("actors/<int:actor_id>/", actor.actor_detail, name="actor_detail"),
]

from threading import Thread
from typing import Any

import requests
from app.models import Actor, Movie
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    This command is used for scraping the best 300 movies from the CSFD asynchronously.
    Due to that, it can be only used for databases, that support concurrency (PostgreSQL, MySQL...).
    """

    CSFD_URLS = [
        "https://www.csfd.cz/zebricky/filmy/nejlepsi?from=1",
        "https://www.csfd.cz/zebricky/filmy/nejlepsi?from=100",
        "https://www.csfd.cz/zebricky/filmy/nejlepsi?from=200",
    ]
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/91.0.4472.124 Safari/537.36"
    }
    help = "Gets top 300 movies from CSFD and saves them into the database"

    def handle(self, *args: Any, **options: Any) -> None:
        self.stdout.write("Gathering of the Movies and Actors has started.")
        threads = []
        for url in self.CSFD_URLS:
            thread = Thread(target=self.scrape_movies_async, args=(url,))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

        self.stdout.write("Movies and actors saved successfully.")

    def scrape_movies_async(self, url: str) -> None:
        response = requests.get(url, headers=self.HEADERS)
        soup = BeautifulSoup(response.text, "html.parser")
        movie_list = soup.find_all("h3", class_="film-title-norating")

        for movie in movie_list:
            movie_title = movie.find("a", class_="film-title-name").text.strip()
            self.stdout.write(f"Operating movie {movie_title}")
            new_movie, _ = Movie.objects.get_or_create(title=movie_title)
            movie_link = "https://www.csfd.cz" + movie.find("a", class_="film-title-name")["href"]
            self.get_movie_actors(movie_link, new_movie)

    def get_movie_actors(self, movie_url: str, movie: Movie) -> None:
        actors = []
        response = requests.get(movie_url, headers=self.HEADERS)
        soup = BeautifulSoup(response.text, "html.parser")
        headline = soup.find("h4", string="Hrají:")
        if headline:
            actors = headline.parent.find_all("a", href=lambda href: href and "/tvurce/" in href)

        for actor in actors:
            actor_name = actor.text.strip()
            actor_obj, _ = Actor.objects.get_or_create(name=actor_name)
            actor_obj.movies.add(movie)

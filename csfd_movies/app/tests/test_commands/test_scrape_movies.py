from unittest import mock

import requests_mock
from app.management.commands.scrape_movies import Command
from app.models import Actor, Movie
from django.core.management import call_command
from django.test import TestCase


class ScrapeMoviesTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.movies_html = """
                <html>
                    <h3 class="film-title-norating">
                        <a class="film-title-name" href="/film/1">Movie 1</a>
                    </h3>
                    <h3 class="film-title-norating">
                        <a class="film-title-name" href="/film/2">Movie 2</a>
                    </h3>
                </html>
            """
        cls.detail_html = """
            <html>
                <h4>Hrají:</h4>
                <a href="/tvurce/1">Actor 1</a>
                <a href="/tvurce/2">Actor 2</a>
            </html>
        """

    def test_handle_command(self):
        with requests_mock.Mocker() as m:
            for url in Command.CSFD_URLS:
                m.get(url, text=self.movies_html)
                m.get("https://www.csfd.cz/film/1", text=self.detail_html)
                m.get("https://www.csfd.cz/film/2", text=self.detail_html)

            call_command("scrape_movies")

            assert len(Movie.objects.all()) == 2
            assert len(Actor.objects.all()) == 2

            movie = Movie.objects.get(title="Movie 1")
            assert len(movie.actors.all()) == 2

    @mock.patch("app.management.commands.scrape_movies.MOVIES_LIMIT", 1)
    def test_limit_not_exceeded(self):
        with requests_mock.Mocker() as m:
            for url in Command.CSFD_URLS:
                m.get(url, text=self.movies_html)
                m.get("https://www.csfd.cz/film/1", text=self.detail_html)
                m.get("https://www.csfd.cz/film/2", text=self.detail_html)

            call_command("scrape_movies")

            assert len(Movie.objects.all()) == 1

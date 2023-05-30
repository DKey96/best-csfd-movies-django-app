from app.models import Movie
from django.test import Client, TestCase
from django.urls import reverse


class MovieDetailViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.movie = Movie.objects.create(title="Test Movie")
        self.movie_detail_url = reverse("movie_detail", args=[self.movie.id])

    def test_movie_detail_view(self):
        response = self.client.get(self.movie_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "movie.html")
        self.assertContains(response, self.movie.title)

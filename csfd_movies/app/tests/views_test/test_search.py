from django.test import Client, TestCase
from django.urls import reverse


class SearchViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.search_url = reverse("search")

    def test_search_view(self):
        response = self.client.get(self.search_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "search.html")

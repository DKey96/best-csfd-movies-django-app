from app.models import Actor
from django.test import Client, TestCase
from django.urls import reverse


class ActorDetailViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.actor = Actor.objects.create(name="Test Actor")
        self.actor_detail_url = reverse("actor_detail", args=[self.actor.id])

    def test_actor_detail_view(self):
        response = self.client.get(self.actor_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "actor.html")
        self.assertContains(response, self.actor.name)

from app.models import Actor
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render


def actor_detail(request, actor_id: int) -> HttpResponse:
    actor_model = get_object_or_404(Actor, id=actor_id)
    return render(request, "actor.html", {"actor": actor_model})

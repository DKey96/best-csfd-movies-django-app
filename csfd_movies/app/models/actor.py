from django.db import models

from app.lib.string_normalization import strip_accents
from app.models.base import ModelWithCSFDId

NAME_MAX_LENGTH = 150


class Actor(ModelWithCSFDId):
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    name_normalized = models.CharField(max_length=NAME_MAX_LENGTH)  # name without diacritics
    movies = models.ManyToManyField("Movie", related_name="actors")

    class Meta:
        indexes = [
            models.Index(fields=["name"])
        ]

    def save(self, *args, **kwargs):
        if not self.name_normalized:
            self.name_normalized = strip_accents(self.name)

        super().save(*args, **kwargs)

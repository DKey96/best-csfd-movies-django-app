from django.db import models

from app.lib.string_normalization import strip_accents
from app.models.base import ModelWithCSFDId

NAME_MAX_LENGTH = 255


class Movie(ModelWithCSFDId):
    title = models.CharField(max_length=NAME_MAX_LENGTH)
    title_normalized = models.CharField(max_length=NAME_MAX_LENGTH)  # title without diacritics

    class Meta:
        indexes = [
            models.Index(fields=["title"])
        ]

    def save(self, *args, **kwargs):
        if not self.title_normalized:
            self.name_normalized = strip_accents(self.title)

        super().save(*args, **kwargs)
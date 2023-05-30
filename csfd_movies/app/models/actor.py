from django.db import models

NAME_MAX_LENGTH = 150


class Actor(models.Model):
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    movies = models.ManyToManyField("Movie", related_name="actors")

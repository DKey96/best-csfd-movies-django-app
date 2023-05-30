from django.db import models

NAME_MAX_LENGTH = 255


class Movie(models.Model):
    title = models.CharField(max_length=NAME_MAX_LENGTH)

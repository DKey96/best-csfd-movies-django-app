from django.db import models


class ModelWithCSFDId(models.Model):
    csfd_id = models.IntegerField(unique=True)

    class Meta:
        abstract = True
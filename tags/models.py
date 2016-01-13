from __future__ import unicode_literals

from django.db import models
from hvad import models as hvad


class Tag(models.Model):
    name = models.CharField(max_length=200)


class Genre(hvad.TranslatableModel):
    translations = hvad.TranslatedFields(
        title = models.CharField(max_length=200)
    )

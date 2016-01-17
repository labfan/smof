from __future__ import unicode_literals

from django.db import models
from hvad import models as hvad
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Genre(hvad.TranslatableModel):
    translations = hvad.TranslatedFields(
            title=models.CharField(max_length=200)
    )

    def __str__(self):
        return self.title

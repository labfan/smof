from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres import fields
from hvad import models as hvad

from actors import models as actors
from tags import models as tags


class ConventionTradition(hvad.TranslatableModel):
    """
    This class represents a convention tradition, say Eastercon.
    The conventions themselves are linked to these models.

    Attributes:
    title:             possibly translatable title of the convention tradition
    description:       translatable description
    genres:            links to genres classification
    tags:              links to tags classification
    awards:            array of fantlab award ids
    link:              URL to convention tradition web-site
    year_established:  year when it was established as a tradition
    """
    translations = hvad.TranslatedFields(
        title=models.CharField(max_length=255),
        description=models.TextField(blank=True, null=True),
    )
    genres = models.ManyToManyField(tags.Genre)
    tags = models.ManyToManyField(tags.Tag)
    awards = fields.ArrayField(models.IntegerField(), blank=True)
    link = models.URLField(blank=True, null=True)
    year_established = models.PositiveSmallIntegerField()


# class Convent(models.Model):
#     traditions = models.ManyToManyField(ConventTradition)
#     title = models.CharField(max_length=255)
#     attendance = models.PositiveSmallIntegerField(choices=())
#     comment = models.TextField()
#
#     genres = models.ManyToManyField(tags.Genre)
#     languages = models.ManyToManyField(i18n.Language)
#     tags = models.ManyToManyField(tags.Tag)
#     awards = models.ManyToManyField(awards.Award)
#
#     location = models.CharField(max_length=255)
#     start_date = models.DateField()
#     end_date = models.DateField()
#
#     participants = models.ManyToManyField(actors.Participant)
#
#
# class Event(models.Model):
#     convent = models.ForeignKey(Convent, on_delete=models.CASCADE)
#
#     tags = models.ManyToManyField(tags.Tag)

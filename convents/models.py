# coding=utf-8
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

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Convention(hvad.TranslatableModel):
    ATTENDANCE_TINY = 1
    ATTENDANCE_SMALL = 2
    ATTENDANCE_NORMAL = 3
    ATTENDANCE_BIG = 4
    ATTENDANCE_HUGE = 5
    ATTENDANCE_CHOICES = (
        (ATTENDANCE_TINY, u'1–10'),
        (ATTENDANCE_SMALL, u'11–30'),
        (ATTENDANCE_NORMAL, u'31–100'),
        (ATTENDANCE_BIG, u'101–1000'),
        (ATTENDANCE_HUGE, u'> 1000'),
    )

    traditions = models.ManyToManyField(ConventionTradition)
    translations = hvad.TranslatedFields(
        title=models.CharField(max_length=255),
        description=models.TextField(blank=True, null=True),
    )

    attendance = models.PositiveSmallIntegerField(choices=ATTENDANCE_CHOICES)
    genres = models.ManyToManyField(tags.Genre)
    tags = models.ManyToManyField(tags.Tag)
    languages = fields.ArrayField(models.CharField(max_length=10), blank=True)
    awards = fields.ArrayField(models.IntegerField(), blank=True)
    link = models.URLField(blank=True, null=True)
    is_bid = models.BooleanField(default=True)

    location = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    participants = models.ManyToManyField(actors.Participant)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# class Event(models.Model):
#     convent = models.ForeignKey(Convent, on_delete=models.CASCADE)
#
#     tags = models.ManyToManyField(tags.Tag)

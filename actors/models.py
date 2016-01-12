from __future__ import unicode_literals

from django.contrib.auth import models as auth
from django.db import models


class Profile(models.Model):
    user = models.ForeignKey(auth.User)


class ProfileToken(models.Model):
    FANTLAB = 'fantlab'
    FACEBOOK = 'facebook'
    VK = 'vk'
    SOURCE_CHOICES = (
        (FANTLAB, FANTLAB),
        (FACEBOOK, FACEBOOK),
        (VK, VK),
    )

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, db_index=True)
    source = models.CharField(choices=SOURCE_CHOICES, max_length=20)
    access_token = models.CharField(max_length=64)
    refresh_token = models.CharField(max_length=64)


class Participant(models.Model):
    profile = models.ForeignKey(Profile,
                                on_delete=models.SET_NULL,
                                blank=True,
                                null=True,
                                db_index=True)

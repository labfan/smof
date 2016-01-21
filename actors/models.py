from __future__ import unicode_literals

from django.contrib.auth import models as auth
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Profile(models.Model):
    user = models.OneToOneField(auth.User)

    def __str__(self):
        return '%s: %d tokens' % (self.user.username, len(self.profiletoken_set.all()))


@python_2_unicode_compatible
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

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.source + ' token'


class Participant(models.Model):
    profile = models.ForeignKey(Profile,
                                on_delete=models.SET_NULL,
                                blank=True,
                                null=True,
                                db_index=True)
    honoured_guest = models.BooleanField(default=False, db_index=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth import models

from actors import models as actors


@receiver(post_save, sender=models.User)
def create_profile(sender, **kwargs):
    actors.Profile.objects.get_or_create(user=kwargs['instance'])


@receiver(post_delete, sender=models.User)
def delete_profile(sender, **kwargs):
    actors.Profile.objects.get(user=kwargs['instance']).delete()

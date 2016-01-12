from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import models as auth

from actors import models


class ProfileInline(admin.StackedInline):
    model = models.Profile
    can_delete = False
    verbose_name_plural = 'profile'


# Define a new User admin
class UserAdmin(auth_admin.UserAdmin):
    inlines = (ProfileInline,)


# Re-register UserAdmin
admin.site.unregister(auth.User)
admin.site.register(auth.User, UserAdmin)

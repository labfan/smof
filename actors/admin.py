from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import models as auth

from actors import models


class ProfileInline(admin.StackedInline):
    model = models.Profile
    verbose_name_plural = 'profile'
    can_delete = False
    show_change_link = True


# Define a new User admin
class UserAdmin(auth_admin.UserAdmin):
    inlines = (ProfileInline,)


class ProfileTokenInline(admin.StackedInline):
    extra = 0
    model = models.ProfileToken
    verbose_name_plural = 'tokens'


class ProfileAdmin(admin.ModelAdmin):
    inlines = (ProfileTokenInline,)
    readonly_fields = ('user',)


# Re-register UserAdmin
admin.site.unregister(auth.User)
admin.site.register(auth.User, UserAdmin)
admin.site.register(models.Profile, ProfileAdmin)

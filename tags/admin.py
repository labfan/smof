from django.contrib import admin
from hvad import admin as hvad_admin

from tags import models


class GenreAdmin(hvad_admin.TranslatableAdmin):
    pass


admin.site.register(models.Tag)
admin.site.register(models.Genre, GenreAdmin)

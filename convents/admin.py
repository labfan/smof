from django.contrib import admin
from hvad import admin as hvad_admin

from convents import models


class ConventionTraditionAdmin(hvad_admin.TranslatableAdmin):
    pass


class ConventionAdmin(hvad_admin.TranslatableAdmin):
    pass


admin.site.register(models.ConventionTradition, ConventionTraditionAdmin)
admin.site.register(models.Convention, ConventionAdmin)

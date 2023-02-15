from django.contrib import admin

from generator.models import Schema, Column


admin.site.register(Schema)
admin.site.register(Column)

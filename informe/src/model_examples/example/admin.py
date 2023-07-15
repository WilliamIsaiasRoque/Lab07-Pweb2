from django.contrib import admin
from .models import Simple, DateExample, NullExample, Character, Movie

admin.site.register(Simple)
admin.site.register(DateExample)
admin.site.register(NullExample)
admin.site.register(Character)
admin.site.register(Movie)

from django.contrib import admin
from .models import Film, DodatkoweInfo, Ocena, Aktor


# Register your models here.
# admin.site.register(Film)

@admin.register(Film)
class FileAdmin(admin.ModelAdmin):
    list_display = ["tytul", "imdb_rating", "rok"]
    list_filter = ("rok", "imdb_rating")
    search_fields = ("tytul", "rok")


admin.site.register(DodatkoweInfo)
admin.site.register(Ocena)
admin.site.register(Aktor)

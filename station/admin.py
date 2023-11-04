from django.contrib import admin

from django.contrib import admin
from .models import Station

@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ['libelle', 'location', 'Nmbr_cuves', 'Nmbr_pompes', 'Nmbr_pompistes']

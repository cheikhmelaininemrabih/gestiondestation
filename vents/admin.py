from django.contrib import admin
from .models import Vente

@admin.register(Vente)
class VenteAdmin(admin.ModelAdmin):
    list_display = ['id_pompe', 'id_pompiste', 'date_vente', 'nv_index', 'anc_index', 'montant_attendu']
    list_filter = ['date_vente']

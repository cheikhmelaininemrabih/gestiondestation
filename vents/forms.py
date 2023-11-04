from django import forms
from .models import Vente

class VenteForm(forms.ModelForm):
    class Meta:
        model = Vente
        fields = ['id_pompe', 'id_pompiste', 'nv_index', 'anc_index', 'montant_attendu', 'image']

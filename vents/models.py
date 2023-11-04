from django.db import models
from django.conf import settings

class Vente(models.Model):
    id_pompe = models.ForeignKey('pompe.Pompe', on_delete=models.CASCADE)
    id_pompiste = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_vente = models.DateTimeField(auto_now_add=True)
    nv_index = models.DecimalField(max_digits=10, decimal_places=2)
    anc_index = models.DecimalField(max_digits=10, decimal_places=2)
    montant_attendu = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='ventes_images/', blank=True, null=True)

    def __str__(self):
        return f"Vente {self.id} - Pompe {self.id_pompe.id}"

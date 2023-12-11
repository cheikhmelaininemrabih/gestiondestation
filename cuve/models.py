from django.db import models
from station.models import Station

class Cuve(models.Model):
    Nb_pmp_alimente = models.IntegerField(null=True)
    charge = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    stocke = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    Qt_min = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    is_active = models.BooleanField(default=True)
    id_station = models.ForeignKey(Station, on_delete=models.CASCADE, null= True, blank= True)

    def __str__(self):
        return f"Cuve {self.id} at {self.id_station.libelle}"
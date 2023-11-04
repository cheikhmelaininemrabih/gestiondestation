from django.db import models
from station.models import Station

class Cuve(models.Model):
    Nb_pmp_alimente = models.IntegerField()
    charge = models.DecimalField(max_digits=10, decimal_places=2)
    stocke = models.DecimalField(max_digits=10, decimal_places=2)
    Qt_min = models.DecimalField(max_digits=10, decimal_places=2)
    id_station = models.ForeignKey(Station, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cuve {self.id} at {self.id_station.libelle}"
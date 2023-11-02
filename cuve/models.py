# cuve/models.py
from django.db import models
from station.models import Station  # Import the Station model if needed

class Cuve(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-incremented primary key
    Nb_pmp_alimente = models.IntegerField()  # Number of pumps supplied
    charge = models.DecimalField(max_digits=10, decimal_places=2)  # Charge in decimal format
    stocke = models.DecimalField(max_digits=10, decimal_places=2)  # Stocke in decimal format
    Qt_min = models.DecimalField(max_digits=10, decimal_places=2)  # Qt_min in decimal format
    id_station = models.ForeignKey(Station, on_delete=models.CASCADE)  # Foreign key to Station model

    def __str__(self):
        return f"Cuve {self.id} at {self.id_station}"


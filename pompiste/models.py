from django.db import models
from station.models import Station 

class Pompiste(models.Model):
    id = models.AutoField(primary_key=True) 
    Nom = models.CharField(max_length=100)
    Prenom = models.CharField(max_length=100)
    Adresse = models.CharField(max_length=200)
    tel = models.CharField(max_length=20)
    id_station = models.ForeignKey(Station, on_delete=models.CASCADE)  
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.Prenom} {self.Nom} at {self.id_station}"

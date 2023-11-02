from django.db import models
from django.contrib.auth.models import User


class Station(models.Model):
    libelle = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    id_users = models.ForeignKey(User, on_delete=models.CASCADE) 
    Nmbr_cuves = models.IntegerField()
    Nmbr_pompes = models.IntegerField()
    Nmbr_pompistes = models.IntegerField()




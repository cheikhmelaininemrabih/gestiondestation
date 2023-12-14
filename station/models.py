from django.db import models
from django.contrib.auth.models import User
from users.models import Profile


class Station(models.Model):
    libelle = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    Nmbr_cuves = models.IntegerField()
    Nmbr_pompes = models.IntegerField()
    Nmbr_pompistes = models.IntegerField()
    responsables = models.ManyToManyField(Profile, related_name='stations' )

    def __str__(self):
        return self.libelle



from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    statut = models.IntegerField(default=0)
    nom = models.CharField(max_length=100)
    # tel = models.CharField(max_length=20)

    @property
    def is_admin(self):
        return self.statut == 0

    @property
    def is_responsable(self):
        return self.statut == 1

    @property
    def is_pompiste(self):
        return self.statut == 2

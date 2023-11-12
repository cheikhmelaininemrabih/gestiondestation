from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role_choices = [
        ('admin', 'Admin'),
        ('responsable', 'Responsable'),
        ('pompiste', 'Pompiste'),
    ]
    role = models.CharField(max_length=20, choices=role_choices)

    # Suppression des champs username, email et password car ils sont déjà inclus dans le modèle User
    tel = models.CharField(max_length=20)

    # Ce champ est inutile car l'email fait partie du modèle User
    # email = models.EmailField(max_length=255)

    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

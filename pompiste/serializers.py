from rest_framework import serializers
from .models import Pompiste

class PompisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pompiste
        fields = ['id', 'Nom', 'Prenom', 'Adresse', 'tel', 'id_station', 'is_active']

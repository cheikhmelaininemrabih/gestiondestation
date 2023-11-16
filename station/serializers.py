from rest_framework import serializers
from .models import Station

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ['libelle', 'location', 'id_users', 'is_active', 'Nmbr_cuves', 'Nmbr_pompes', 'Nmbr_pompistes']

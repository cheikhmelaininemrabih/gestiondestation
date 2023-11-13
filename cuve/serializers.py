from rest_framework import serializers
from .models import Cuve

class CuveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuve
        fields = ['id', 'Nb_pmp_alimente', 'charge', 'stocke', 'Qt_min', 'is_active', 'id_station']

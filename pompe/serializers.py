from rest_framework import serializers
from .models import Pompe

class PompeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pompe
        fields = ['id', 'type', 'model', 'id_cuve', 'id_pompiste', 'is_active']

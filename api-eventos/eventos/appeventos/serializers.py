from rest_framework import serializers 
from .models import Evento

#O modelo Evento irá ser convertido para json

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'
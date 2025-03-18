from rest_framework import serializers 
from .models import Carro 

#O modelo Carro irá ser convertido para json
class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carro
        fields = '__all__'
        
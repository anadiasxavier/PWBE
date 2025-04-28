from rest_framework import serializers 
from .models import UsuarioDS16
#o serializer está transformando o model usuarioDS16 em json

class usuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioDS16
        fields = '__all__'
        
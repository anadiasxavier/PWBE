#imports
from rest_framework import serializers
from .models import Usuario, Empresa , Ingresso
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer 

#criando os serializers
#serializer UsuarioSerializer
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario #pega o modelo que ira serializar
        fields = '__all__'

#serializer Empresaerializer
class Empresaerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

#serializer LoginSerializer
class LoginSerializer(TokenObtainPairSerializer): 
    def validate(self, attrs):
        data = super().validate(attrs) #o super() está chamando o token, validação.
        data['usuario'] = {
            'id': self.user.id,
            'username': self.user.username,
        }
        return data
    

#serializer do ingresso
class IngressoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingresso
        fields = '__all__'
        
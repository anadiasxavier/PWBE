from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import UsuarioSerializer , IngressoSerializer, LoginSerializer
from .permissions import IsGestor , IsGestorOuDono 
from rest_framework.permissions import IsAuthenticated
from .models import Usuario, Ingresso
from rest_framework_simplejwt.views import TokenObtainPairView

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

class UsuarioListCreateAPIView(ListCreateAPIView):
    queryset =  Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsGestor]

class IngressoRUDAPI(RetrieveUpdateDestroyAPIView):
    queryset = Ingresso.objects.all()
    serializer_class = IngressoSerializer
    permission_classes = [IsGestorOuDono]

class IngressoListCreateAPIView(ListCreateAPIView):
    queryset = Ingresso.objects.all()
    serializer_class = IngressoSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()] #AllowAny, para que todos consiga ver, é o padrão
        return [IsGestor()]
    
'''    #permission_classes = [IsGestor]
    #Permitir quem for autenticado fazer o GET, ou o Gestor
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsGestor()]
    #o queryset tambem seria usado aqui '''
    
'''class IngressoRetrieveUpdateDestroyAPIView(RetriveUpdateDestroyAPIView):
    queryset = Ingresso.objects.all() #filtra pelo id 
    serializer_class = IngressoSerializer
    permission_classes = [IsGestorOuDono]
    look_field = 'pk'''
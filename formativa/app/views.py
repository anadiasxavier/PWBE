from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, ListCreateAPIView , RetrieveUpdateDestroyAPIView, ListAPIView
from .models import Usuario, Disciplina, ReservaAmbiente
from .serializers import UsuarioSerializer, DisciplinaSerializer , ReservaAmbienteSerializer,  LonginSerializer
from .permissions import IsGestor , IsProfessor , IsDonoOuGestor
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

class UsuarioListCreat (ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsGestor]

# Class que ira deletar, visualizar um em expecifico  e atualixar
class UsuarioRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsGestor]
    lookup_field = 'pk' 

# Listar Todas e criar disciplina
class DisciplinaListCreate(ListCreateAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsGestor]

# Class que ira deletar, visualizar um em expecifico  e atualizar Disciplina
class DisciplinaRetrieveUpdateDestroy(UsuarioRetrieveUpdateDestroyAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    permission_classes = [IsGestor]
    lookup_field = 'pk'


#Listar disciplinas do professor
class DisciplinaProfessorList(ListCreateAPIView):
    serializer_class = DisciplinaSerializer
    permission_classes = [IsProfessor]

    def get_queryset(self):
        return Disciplina.objects.filter(professor = self.request.user)

#Visualizar todos e criar
class ReservaAmbienteListCreate(ListCreateAPIView):
    queryset = ReservaAmbiente.objects.all()
    serializer_class = ReservaAmbienteSerializer

    #define as permissoes
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsGestor()]
    
    #consulta de modo personalizado, se caso passar o id do professor 
    def get_queryset(self):
        queryset = super().get_queryset()
        professor_id = self.request.query_params.get('professor', None)
        if professor_id:
            queryset = queryset.filter(professor_id=professor_id)
        return queryset 

class ReservaAmbienteRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
        queryset = ReservaAmbiente.objects.all()
        serializer_class = ReservaAmbienteSerializer
        permission_class = [IsDonoOuGestor]
        lookup_field = 'pk'

class ReservaAmbienteProfessorList (ListAPIView):
    serializer_class = ReservaAmbienteSerializer
    permission_class = [IsProfessor]

    def get_queryset(self):
        return ReservaAmbiente.objects.filter(professor= self.request.user)

class LoginView(TokenObtainPairView):
    serializer_class = LonginSerializer
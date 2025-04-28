from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Piloto
from .models import Carro
from .serializers import CarroSerializer
from .serializers import PilotoSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import serializers
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# o @sswagger_auto_schema é para a documentação

# views para o piloto
# define o tamanho da pagina e quantos pilotos ira aparecer
class PilotoPaginacao(PageNumberPagination):
    page_size = 5
    page_size_query_param ='page_size'
    max_page_size = 10

#Deleta, Atualiza atraves do id fornecido
class PilotoRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Piloto.objects.all()
    serializer_class = PilotoSerializer
    lookup_field= 'pk'

    @swagger_auto_schema(
         operation_description= 'Pega o piloto do ID fornecido',
         responses={
              200: PilotoSerializer,
              404 : 'NoT Found',
              400: 'Error'
         }
    )
    def get(self, request, *args, **kwargs):
            return super().get(request, *args, **kwargs) 
# ate aqui,para delete  e update e patch

#PilotoListCreateAPIView para listar
class PilotoListCreateAPIView(ListCreateAPIView):
    queryset = Piloto.objects.all()
    serializer_class = PilotoSerializer
    pagination_class = PilotoPaginacao

    @swagger_auto_schema(
            operation_description='Lista todos os pilotos de Formula 1',
            responses={
                200: PilotoSerializer(many=True),
                400: 'Error'
            },

            manual_parameters=[
                openapi.Parameter(
                    'nome',
                    openapi.IN_QUERY,
                    description='Filtrar pelo nome do piloto',
                    type=openapi.TYPE_STRING
                )
            ]
        )
    
    def get(self, request, *args, **kwargs):
            return super().get(request, *args, **kwargs) 

    
    @swagger_auto_schema(
        operation_description='Cria um novo piloto',
        request_body= PilotoSerializer,
        responses={
            201: PilotoSerializer,
            400: 'ERROOOO'
        }
    )

    def post(self, request, *args, **kwargs):
            return super().post(request, *args, **kwargs) 
    
    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.query_params.get('nome')
        if nome: 
            queryset = queryset.filter(nome__icontains = nome)
        return queryset
    
    def perform_create(self, serializer):
       if serializer.validated_data['equipe'] != 'DS16' and serializer.validated_data['classificacao'] <=5:
           raise serializers.ValidationError('Somente a DS16 deve ficar entre os 5')
       serializer.save()

# views do carro 
# define o tamanho da pagina e quantos carro ira aparecer
class CarroPaginacao(PageNumberPagination):
    page_size = 5
    page_size_query_param ='page_size'
    max_page_size = 10
    
#Deleta, Atualiza atraves do id fornecido
class CarroRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer
    lookup_field= 'pk'

    @swagger_auto_schema(
            operation_description= 'Pega o carro do ID fornecido',
            responses={
                200: CarroSerializer,
                404 : 'NoT Found',
                400: 'Error'
            }
        )
    def get(self, request, *args, **kwargs):
                return super().get(request, *args, **kwargs)
# ate aqui,para delete  e update e patch

#CarroListCreateAPIView para listar
class CarroListCreateAPIView(ListCreateAPIView):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer
    # pagination_class = CarroPaginacao
    def get_queryset(self):
        queryset = super().get_queryset()
        
        nome = self.request.query_params.get('nome')
        if nome: 
            queryset = queryset.filter(nome__icontains = nome)
        return queryset

    @swagger_auto_schema(
            operation_description='Lista todos os carros de Formula 1',
            responses={
                200: CarroSerializer(many=True),
                400: 'Error'
            },

            manual_parameters=[
                openapi.Parameter(
                    'nome',
                    openapi.IN_QUERY,
                    description='Filtrar pelo nome do carro',
                    type=openapi.TYPE_STRING
                )
            ]
        )
    
    def get(self, request, *args, **kwargs):
            return super().get(request, *args, **kwargs) 

 
    @swagger_auto_schema(
        operation_description='Cria um novo carro',
        request_body= CarroSerializer,
        responses={
            201: CarroSerializer,
            400: 'ERROOOO'
        }
    )

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs) 
    
    
    

    
    
 
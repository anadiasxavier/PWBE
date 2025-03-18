from django.shortcuts import render
from .models import Carro
from .serializers import CarroSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Nas views foram utilizadas a api_view.

# No read_carros foi usado o método GET, ela foi feita para ler a lista dos carros criados.
@api_view(['GET'])
def read_carros(request):
    carros = Carro.objects.all()
    serializer = CarroSerializer(carros, many = True)
    return Response(serializer.data)

# No pegar_carro também foi usado o método GET, porém é para vizualizar apenas um carro, também foi feito uma mensagem de erro.
@api_view(['GET'])
def pegar_carro(request, pk):
    try:
        carro = Carro.objects.get(pk=pk)
    except Carro.DoesNotExist: #mensagem de erro
        return Response({'erro': 'Carro inexistente'}, status=status.HTTP_404_NOT_FOUND)

    serializer = CarroSerializer(carro)
    return Response(serializer.data)

#No create_carro foi utilizado o método POST, aqui é possivel que o usuario crie um carro e ele é colocado na lista de carros existentes.
@api_view(['POST'])
def create_carro(request):
    if request.method == 'POST':
        serializer = CarroSerializer(data=request.data, many=isinstance(request.data, list))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST) #Mensagem de erro

#No update_carro foi utilizado o método PUT, opção feita para atualizar alguma infomação de algum carro já existente.  
@api_view(['PUT'])
def update_carro(request, pk):
    try:
        carro = Carro.objects.get(pk=pk)
    except Carro.DoesNotExist:
        return Response({'erro': 'Carro inexistente'}, status=status.HTTP_404_NOT_FOUND) #Mensagem de erro
    
    serializer = CarroSerializer(carro, data=request.data)
    if serializer.is_valid():
        serializer.save() #aqui as informações são salvas e a lista é atualizadas.
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#No delete_carro é utilizado o método DELETE, opção feita para excluir algum carro existente.
@api_view(['DELETE'])
def delete_carro(request, pk):
    try:
        carro = Carro.objects.get(pk=pk)
    except Carro.DoesNotExist:
        return Response({'erro': 'Carro inexistente'}, status=status.HTTP_404_NOT_FOUND) #se o carro não existir a mensagem de erro é enviada.
    
    carro.delete()
    return Response({'Mensagem': f'O seu {carro.nome} foi apagado'}, status=status.HTTP_200_OK) #O carro é excluido e a lista é atualizada.

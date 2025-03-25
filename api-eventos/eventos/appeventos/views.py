from django.shortcuts import render
from .models import Evento
from .serializers import EventoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from datetime import datetime, timedelta

#utilizei nas views a api_view


#No categorias_eventos foi usado o método GET, ela mostra ao usuario a lista de eventos em determinada categoria / data.
@api_view(['GET'])
def categorias_eventos(resquest):

    #Filtrar eventos por categoria
    eventos = Evento.objects.all()
    categoria = resquest.query_params.get('categoria')
    if categoria:
        eventos = eventos.filter(categoria__icontains = categoria)

    #Filtrar eventos por data
    datatime = resquest.query_params.get('datatime')
    if datatime:
        eventos = eventos.filter(datatime__icontains = datatime)
    
    #Aparecer os  primeiros eventos para o usuario
    quantidade = resquest.query_params.get('quantidade')
    if quantidade:
     eventos = eventos[:int(quantidade)]

    #Ordenar eventos por datas
    ordem = resquest.query_params.get('ordem')
    if ordem:
        eventos = eventos.order_by('datatime') 
    
    #Caso o evento não exista
    if not eventos.exists():
        return Response({"Mensagem": "Esse evento não existe!"}, status=status.HTTP_200_OK)
    serializer = EventoSerializer (eventos , many = True)
    return Response(serializer.data)

#No ordem_eventos foi utlizado o metodo GET, ela mostra ao usuario os eventos dos proximos dias. O usuario que escolhe os dias pelo parametro
@api_view(['GET'])
def ordem_eventos(resquest):
    eventos = Evento.objects.all()
    proximos = resquest.query_params.get('proximos')
    if proximos:
        agora = datetime.now()
        dataCom7 = agora + timedelta(days=int(proximos))
        eventos = eventos.filter(datatime__gte=agora, datatime__lte =dataCom7 ) 

    #Caso o evento não exista
        if not eventos.exists():
            return Response({"Mensagem": "Não temos eventos para essa data!"}, status=status.HTTP_200_OK)
    serializer = EventoSerializer (eventos , many = True)
    return Response(serializer.data)

    
#No pegar_eventos também foi usado o método GET, porém aqui seria uma busca, o usuario coloca a chave do evento para procurar.
@api_view(['GET'])
def pegar_eventos(request, pk):
    try:
        eventos = Evento.objects.get(pk=pk)
    except Evento.DoesNotExist: #mensagem de erro
        return Response({'erro': 'Evento inexistente'}, status=status.HTTP_404_NOT_FOUND)
    serializer = EventoSerializer(eventos)
    return Response(serializer.data)

#No create_evento foi utilizado o método POST, aqui é possivel que o usuario crie um evento e ele é colocado na lista de eventos existentes.
@api_view(['POST'])
def create_evento(request):
    if request.method == 'POST':
        serializer = EventoSerializer(data= request.data, many = isinstance (request.data, list))
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST) #Mensagem de erro
    
#No update_evento foi utilizado o método PUT, opção feita para atualizar alguma infomação de algum evento já existente.  
@api_view(['PUT'])
def update_evento(resquest, pk):
    try:
        eventos = Evento.objects.get(pk=pk)
    except Evento.DoesNotExist:
        return Response({'erro': 'Evento inexistente'}, status=status.HTTP_404_NOT_FOUND) #Mensagem de erro
    
    serializer = EventoSerializer(eventos , data=resquest.data)
    if serializer.is_valid():
        serializer.save()#aqui as informações são salvas e a lista é atualizadas.
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#No delete_evento é utilizado o método DELETE, opção feita para excluir algum evento existente.
@api_view(['DELETE'])
def delete_evento(request, pk):
    try:
        eventos = Evento.objects.get(pk=pk)
    except Evento.DoesNotExist:
        return Response({'erro': 'Evento inesxistente'}, status=status.HTTP_404_NOT_FOUND)#se o evento não existir a mensagem de erro é enviada.
    
    eventos.delete()
    return Response({'Mensagem': f'O seu {eventos.nome} foi apagado'}, status=status.HTTP_200_OK)#O evento é excluido e a lista é atualizada.
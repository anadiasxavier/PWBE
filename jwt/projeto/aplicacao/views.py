#imports das views
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import UsuarioDS16
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .serializers import usuarioSerializer

#Criacao do criar_usuario, foi utilizado o metodo post
@api_view(['POST'])
def criar_usuario(request):
    username = request.data.get('username')
    senha = request.data.get('senha')
    biografia = request.data.get('biografia')
    telefone = request.data.get('telefone')
    idade = request.data.get('idade')
    endereco = request.data.get('endereco')
    escolaridade = request.data.get('escolaridade')
    quant_animal = request.data.get('quant_animal')

    # Informações da atividade passadas
    # edv = request.data.get('EDV')
    # data_nascimento = request.data.get('data_nascimento')
    # padrinho = request.data.get('padrinho')
    # apelido = request.data.get('apelido')

    #mensagem de erro
    if not username or not senha or not telefone or not endereco:
        return Response({'Erro': 'Campos obrigatorios incompleto'}, status = status.HTTP_400_BAD_REQUEST)

    if UsuarioDS16.objects.filter(username=username).exists():
        return Response({'Erro': f'Username {username} já existe'}, status=status.HTTP_400_BAD_REQUEST)
    
    
    usuario = UsuarioDS16.objects.create_user(
       username=username,
       password= senha,
       biografia =biografia,
       telefone = telefone,
       idade= idade,
       endereco = endereco,
       escolaridade = escolaridade,
       quant_animal = quant_animal,
       
    )
    return Response({'Mensagem': f'Usuario {username} criado com sucesso' }, status=status.HTTP_201_CREATED)

#Criacao do logar_usuario, foi utilizado o metodo post
#é usado para o usuario logar
@api_view(['POST'])
def logar_usuario(request):
    username = request.data.get('username')
    senha = request.data.get('senha')
    print(username, senha)
    usuario = authenticate(username = username, password= senha)

    if usuario:
        refresh = RefreshToken.for_user(usuario)

        return Response({
            'acesso': str(refresh.access_token),
            'refresh': str (refresh)
        }, status = status.HTTP_200_OK)
    else:
        return Response({'Erro': 'Usuario ou/e senha incorreto(s)'},status=status.HTTP_401_UNAUTHORIZED) 
        #mensagem de erro
#Criacao do red, foi utilizado o metodo get, feito para ler os usuarios
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read(request):
   usuarios = UsuarioDS16.objects.all()
   serializer = usuarioSerializer (usuarios, many = True)
   return Response ({'users':serializer.data}, status=status.HTTP_200_OK)

# atualizar
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_usuarios(request, pk):
    try:
        usuarios = UsuarioDS16.objects.get(pk=pk)
    except UsuarioDS16.DoesNotExist:
        return Response({'erro': 'Usuario inexistente'}, status=status.HTTP_404_NOT_FOUND) #Mensagem de erro
    serializer = usuarioSerializer(usuarios, data=request.data)
    if serializer.is_valid():
        serializer.save() #aqui as informações são salvas e a lista é atualizadas.
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Deletar
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_usuarios(request, pk):
    try:
        usuarios = UsuarioDS16.objects.get(pk=pk)
    except UsuarioDS16.DoesNotExist:
        return Response({'erro': 'Usuario inexistente'}, status=status.HTTP_404_NOT_FOUND) 
    
    usuarios.delete()
    return Response({'Mensagem': f'O seu usuario foi apagado'}, status=status.HTTP_200_OK) 


#  {
#  "username": "Ana",
#  "password": "123",
#  "biografia": "lalalallalalalalalala",
#  "telefone": "1264758-54876",
#  "idade": 18,
#  "endereco": "fhrgssjjgbsxzkweosd",
#  "escolaridade": "Ensino medio",
#  "quant_animal": 2
#  }


#   {
#   "username": "dias",
#   "senha": "Ac020107@"
#   }
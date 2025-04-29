from django.db import models
from django.contrib.auth.models import AbstractUser #usado para criar um usuario personalizado

#Criacao do models, Empresa
class Empresa(models.Model):
    #atributos
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=100)


#Criacao do models, usuario
class Usuario(AbstractUser):
    #atributos
    apelido = models.CharField(max_length=100, null=True, blank=True)
    telefone = models.CharField(max_length=100, null=True, blank=True)
    genero = models.CharField(max_length=100, choices=(('M', 'Masculino'), ('F', 'Feminino'), ('N', 'Prefiro não informar')), null=True, blank=True)

    escolha_colaborador =(
        ('G', 'Gestor'),
        ('E', 'Estagiario'),
        ('A', 'Aprendiz'),
        ('M', 'Meio oficial')
    )

    colaborador = models.CharField(max_length=1, choices=escolha_colaborador, default='A') #O default é para quando a pessoa não colocar o valor, ele dará esse valor, no caso Aprendiz
    REQUIRED_FIELDS = ['colaborador'] #campo obrigatorio

    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True, blank=True)


#ana
#ana123

#admin
#123
#exemplo para formativa
class Ingresso(models.Model):
    nome = models.CharField(max_length=100)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE) #aqui seria, um usuario pode ter varios ingressos, ai tem que utilizar a chave estrageira

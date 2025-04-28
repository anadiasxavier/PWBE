#A model foi criada
from django.db import models
from django.contrib.auth.models import AbstractUser

class UsuarioDS16(AbstractUser):
    #os atributos da model foi definida
    biografia = models.CharField(max_length=255, null=True, blank=True)
    idade = models.PositiveIntegerField(null=True, blank=True)
    telefone = models.CharField(max_length=255, null=True, blank=True)
    endereco = models.CharField(max_length=255, null=True, blank=True)
    escolha_escolaridade = (
        ('ENSINO MEDIO', 'Ensino Medio'),
        ('ENSINO FUNDAMENTAL', 'Ensino Fundamental'),
        ('ENSINO TECNICO', 'Ensino Tecnico'),
        ('ENSINO SUPERIOR', 'Ensino superior'),
    )
    escolaridade = models.CharField(max_length=20, choices=escolha_escolaridade)
    quant_animal = models.PositiveIntegerField(null=True, blank=True)
    #campo obrigadorio 
    REQUIRED_FIELDS = ['telefone', 'endereco']

    # Informações da atividade anterior
    # data_nascimento = models.DateField()
    # edv = models.PositiveIntegerField()
    # padrinho = models.CharField(max_length=255, null=True, blank=True)
    # apelido = models.CharField(max_length=255, null=True, blank= True)
    # REQUIRED_FIELDS = ['data_nascimento', 'edv', ] 
    # Tudo que for obrigatorio colocar dentro do required_fields

    def __str__(self):
        return self.username
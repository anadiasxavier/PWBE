from django.db import models

class Tarefa(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    status = models.CharField(max_length=100)

def __str__(self):
    return self.titulo
# Create your models here.

from django.db import models


# O modelo Evento foi criado, ele é utilizado em diversos outros arquivos.
class Evento(models.Model):
    nome = models.CharField(max_length= 255)
    descricao = models.TextField()
    datatime = models.DateTimeField()
    local = models.CharField(max_length=255, blank = True)
    escolhas_categoria = (
        ('MÚSICA', 'Música'),
        ('PALESTRA', 'Palestra'),
        ('WORKSHOP', 'Workshop'),
    )

    categoria = models.CharField(max_length= 9 , choices=escolhas_categoria)

    def __str__(self):
        return self.nome


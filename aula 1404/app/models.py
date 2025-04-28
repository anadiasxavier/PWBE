from django.db import models
# criando os models piloto e carro 
class Piloto(models.Model):
    nome = models.CharField(max_length= 255)
    idade = models.PositiveIntegerField()
    classificacao = models.PositiveIntegerField()
    equipe = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.nome} está na {self.classificacao} posição'

class Carro(models.Model):
    nome = models.CharField(max_length=255)
    marca = models.CharField(max_length=255)
    velocidade_maxima = models.PositiveIntegerField()
    cor = models.CharField(max_length=50)
    escolhas_cores =(
        ('VERMELHO', 'Vermelho'),
        ('ROSA', 'Rosa'),
        ('BRANCO', 'Branco'),
        ('DOURADO', 'Dourado'),
        ('ROXO', 'Roxo'),
        ('CINZA', 'Cinza'),
    )
    cor = models.CharField(max_length=50, choices=escolhas_cores)
    piloto = models.ForeignKey(Piloto, on_delete=models.CASCADE)

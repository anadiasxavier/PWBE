from django.shortcuts import render
from .models import Tarefa

def lista_tafera(request):
    tarefa = Tarefa.objects.all().order_by('-status')
    return render(request, 'tarefa/lista_taref.html', {'Tarefa': tarefa})
# Create your views here.

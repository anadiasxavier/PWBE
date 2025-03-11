from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro
from .forms import ItemForm

# Comecei a criar diferentes def para depois utilizar no html, tem a def de lista_livro que é para que o usuario consiga ver a lista.
def lista_livro(request):
    lista = Livro.objects.all().order_by('-data_criacao')
    return render(request, 'blog/lista_livro.html', {'lista': lista})

# Essa def é para criar um novo livro e adicionar na lista_livro
def lista_create(request):
    if request.method == 'POST':
        lista = ItemForm(request.POST)
        if lista.is_valid():
            lista.save()
            return redirect('lista_livro')
            
    else:
        lista= ItemForm()
    return render(request, 'blog/lista_read.html', {'lista': lista})

#Já nessa def ela irá editar o livro, e depois salvar na lista_livro
def lista_update(request, pk):
    
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        lista = ItemForm(request.POST, instance=livro)
        if lista.is_valid():
            lista.save()
            return redirect('lista_livro')
    else:
        lista = ItemForm(instance=livro)
    return render(request, 'blog/lista_read.html', {'lista': lista})

#Essa def serve para deletar o livro da lista.
def lista_delete(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        livro.delete()
        return redirect('lista_livro')
    return render (request, 'blog/confirmar_delete.html', {'livro': livro})

#Por ultimo, temos essa def que filtra o input do usuario.
def lista_livros(request):
    autor = request.GET.get('autor', '')
    if autor:
        livros = Livro.objects.filter(autor__icontains=autor)
    else:
        livros = Livro.objects.all()  
    return render(request, 'blog/lista_livro.html', {'lista': livros})
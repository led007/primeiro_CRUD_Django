

from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto
from .forms import ProdutoForm

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/lista_produtos.html', {'produtos': produtos})

def detalhes_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    return render(request, 'produtos/detalhes_produto.html', {'produto': produto})

def novo_produto(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            produto = form.save(commit=False)
            produto.save()
            return redirect('detalhes_produto', pk=produto.pk)
    else:
        form = ProdutoForm()
    return render(request, 'produtos/editar_produto.html', {'form': form})

def editar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == "POST":
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            produto = form.save(commit=False)
            produto.save()
            return redirect('detalhes_produto', pk=produto.pk)
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produtos/editar_produto.html', {'form': form})

def deletar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    produto.delete()
    return redirect('lista_produtos')

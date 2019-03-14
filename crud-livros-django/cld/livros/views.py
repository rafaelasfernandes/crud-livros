from django.shortcuts import render
from django.http import HttpResponse
from .models import Livro

from . import urls
# Create your views here.

def index(request):
    return HttpResponse("Olá, Mundo. Você está na página index de livros")

def livro_list(request):
    livros = Livro.objects.order_by('titulo')
    return render(request, 'livros/livro_list.html', {'livros' : livros}, {})

from django.shortcuts import render
from sitedemoday.models import Candidato
from sitedemoday.forms import CriarCadastro
# Create your views here.

def todos_candidatos(request):
    candidatos = Candidato.objects.all()

    contexto = {
        'candidatos': candidatos
    }
    
    return render(request, 'todos_candidatos.html', contexto)


def cadastro_candidato(request):
    formulario = CriarCadastro(request.POST or None)
    
    if formulario.is_valid():
        formulario.save()
        formulario = CriarCadastro()

    contexto = {
        'form': formulario
    }

    return render(request, 'novo_candidato.html', contexto)

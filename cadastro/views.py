from django.shortcuts import render
from cadastro.models import Empresa
from cadastro.forms import CadastroEmpresa

# Create your views here.
def todos_candidatos(request):
    vagas = Empresa.objects.all()

    contexto = {
        'vagas': candidatos
    }
    
    return render(request, 'vagas.html', contexto)



def criar_cadastro(request):
    formulario = CadastroEmpresa(request.POST or None)
 
    if formulario.is_valid():
        formulario.save()
        formulario = CadastroEmpresa()

    contexto = {
        'form': formulario
    }

    return render(request, 'novo_cadastro.html', contexto)


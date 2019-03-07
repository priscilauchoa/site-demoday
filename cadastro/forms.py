from django import forms
from cadastro.models import Empresa

class CadastroEmpresa(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = [
             'nome_fantasia',
             'razao_social',
             'CNPJ',
             'descricao_da_empresa',
             'porte_da_empresa',
             'endereco',
             'telefone',
             'site',
             'cargo',
             'descricao_da_vaga',
             'requisitos',
             'carga_horaria',
             'beneficios',
             'local_de_trabalho'
        ]
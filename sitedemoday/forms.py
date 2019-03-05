from django import forms
from sitedemoday.models import Candidato

class CriarCadastro(forms.ModelForm):
    class Meta:
        model = Candidato
        fields = [
            'nome',
            'telefone',
            'celular',
            'email',
            'endereco',
            'experiencia_prof'
        ]
        
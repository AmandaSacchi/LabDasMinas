from django import forms
from meusite.models import Candidato #nao cadastrar produto, apenas pedido

class CandidatoForm(forms.ModelForm):
    class Meta:
        model = Candidato    
        fields = [    #campos do formulario
            'nome',
            'idade',
            'genero',
            'data_nascimento',
            'nacionalidade',
            'ja_trabalha',
            'pretencao_salarial',
            'conhecimentos',
            'educacao',
            'perfil'
        ]


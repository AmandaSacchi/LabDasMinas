from django.db import models
from datetime import date

class Candidato(models.Model):
    
    genero_feminino = 'f'
    genero_masculino = 'm'
    genero_outro = 'o'

    genero_opcoes = [
        (genero_feminino, 'Feminino'),
        (genero_masculino, 'Masculino'),
        (genero_outro, 'Outro'),
    ]

    nome = models.CharField(max_length=100, default="Nome Completo")
    idade = models.IntegerField()
    genero = models.CharField(max_length=11, choices=genero_opcoes, default=" ")
    data_nascimento = models.DateField(default = date.today)
    nacionalidade = models.CharField(max_length=50, default="Brasil")
    ja_trabalha = models.BooleanField(default=True)
    pretencao_salarial = models.DecimalField(decimal_places=2, max_digits=1000, default=0.00)
    conhecimentos = models.TextField(max_length=10000, default = "Coloque aqui suas habilidades e aptidões")
    educacao = models.TextField(max_length=10000, default = "Coloque aqui quais cursos você já fez e quando foram finalizados")
    perfil = models.TextField(max_length=10000, default = "Coloque aqui suas experiencias proficionais, cargos")

    def __str__ (self):
        return self.nome


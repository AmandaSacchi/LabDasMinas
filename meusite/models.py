from django.db import models

# Create your models here.

class Candidato(models.Model):
    genero_opcoes = [
        ("Feminino", 'Feminino'),
        ("Masculino", 'Masculino'),
        ("Outro", 'Outro'),
    ]

    nome = models.CharField(max_length=100, default="")
    idade = models.IntegerField()
    genero = models.CharField(max_length=15, choices=genero_opcoes, default="")
    data_nascimento = models.DateField()
    nacionalidade = models.CharField(max_length=50, default="")
    ja_trabalha = models.BooleanField(default=True)
    pretencao_salarial = models.DecimalField(decimal_places=2, max_digits=1000, default=0)
    perfil = models.TextField(default="")
    foto = models.ImageField(upload_to='', null=True)

    def __str__ (self):
        return self.nome


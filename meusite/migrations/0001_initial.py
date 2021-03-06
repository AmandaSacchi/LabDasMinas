# Generated by Django 2.2.1 on 2019-05-20 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default=' ', max_length=100)),
                ('idade', models.IntegerField()),
                ('genero', models.CharField(choices=[('f', 'Feminino'), ('m', 'Masculino'), ('o', 'Outro')], default=' ', max_length=11)),
                ('nacionalidade', models.CharField(default=' ', max_length=50)),
                ('ja_trabalha', models.BooleanField(default=True)),
                ('pretencao_salarial', models.DecimalField(decimal_places=2, default=0, max_digits=1000)),
                ('perfil', models.TextField(default=' ')),
                ('foto', models.ImageField(null=True, upload_to='')),
            ],
        ),
    ]

# Generated by Django 2.2.1 on 2019-05-21 16:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meusite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidato',
            name='data_nascimento',
            field=models.DateField(default=datetime.date.today),
        ),
    ]

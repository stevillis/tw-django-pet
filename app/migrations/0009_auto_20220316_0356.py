# Generated by Django 3.2.12 on 2022-03-16 07:56

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20220315_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='cargo',
            field=models.IntegerField(choices=[(1, 'Veterinário'), (2, 'Financeiro'), (3, 'Atendimento')], default=3),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='data_nascimento',
            field=models.DateField(default=datetime.date(2022, 3, 16)),
        ),
    ]

# Generated by Django 3.2.12 on 2022-03-15 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_consulta_peso_atual'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=100)),
                ('data_nascimento', models.DateField()),
                ('cargo', models.IntegerField(choices=[(1, 'Veterinário'), (2, 'Financeiro'), (3, 'Atendimento')])),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

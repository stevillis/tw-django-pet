# Generated by Django 3.2.12 on 2022-03-15 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_consulta'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='consulta',
            options={'ordering': ['-created']},
        ),
        migrations.RemoveField(
            model_name='consulta',
            name='data',
        ),
    ]

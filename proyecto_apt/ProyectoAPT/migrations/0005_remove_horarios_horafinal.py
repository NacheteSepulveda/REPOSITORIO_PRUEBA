# Generated by Django 4.2.7 on 2024-09-30 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoAPT', '0004_tipotratamiento_alter_horarios_tipotratamiento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='horarios',
            name='HoraFinal',
        ),
    ]
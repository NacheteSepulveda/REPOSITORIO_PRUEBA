# Generated by Django 4.2.7 on 2024-10-31 17:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoAPT', '0006_cita_direccion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='horarios',
            options={'verbose_name': 'Horario', 'verbose_name_plural': 'Horarios'},
        ),
        migrations.AddField(
            model_name='horarios',
            name='fin',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='horarios',
            name='estudiante',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='horarios_estudiante', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='horarios',
            name='paciente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='horarios_paciente', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='horarios',
            name='tipoTratamiento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ProyectoAPT.tipotratamiento'),
        ),
    ]

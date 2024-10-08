# Generated by Django 4.2.7 on 2024-09-30 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoAPT', '0003_alter_customuser_id_alter_horarios_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tipoTratamiento',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombreTratamiento', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='horarios',
            name='tipoTratamiento',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ProyectoAPT.tipotratamiento'),
        ),
    ]

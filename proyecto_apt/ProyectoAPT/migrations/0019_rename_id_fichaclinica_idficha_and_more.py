# Generated by Django 4.2.7 on 2024-10-18 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoAPT', '0018_fichaclinica_paciente'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fichaclinica',
            old_name='id',
            new_name='idFicha',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='diagnostico',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='fecha_ultima_consulta',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='motivo_consulta',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='nombre_contacto_emergencia',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='proxima_cita',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='relacion_paciente',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='sintomas_actuales',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='telefono_contacto_emergencia',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='tratamiento_actual',
        ),
        migrations.RemoveField(
            model_name='fichaclinica',
            name='correo_electronico',
        ),
        migrations.RemoveField(
            model_name='fichaclinica',
            name='direccion',
        ),
        migrations.RemoveField(
            model_name='fichaclinica',
            name='edad',
        ),
        migrations.RemoveField(
            model_name='fichaclinica',
            name='estado_civil',
        ),
        migrations.RemoveField(
            model_name='fichaclinica',
            name='fecha_nacimiento',
        ),
        migrations.RemoveField(
            model_name='fichaclinica',
            name='nombre_completo',
        ),
        migrations.RemoveField(
            model_name='fichaclinica',
            name='relacion_paciente',
        ),
        migrations.RemoveField(
            model_name='fichaclinica',
            name='rut',
        ),
        migrations.RemoveField(
            model_name='fichaclinica',
            name='sexo',
        ),
        migrations.RemoveField(
            model_name='fichaclinica',
            name='telefono',
        ),
        migrations.AlterField(
            model_name='fichaclinica',
            name='nombre_contacto_emergencia',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='fichaclinica',
            name='telefono_contacto_emergencia',
            field=models.IntegerField(),
        ),
    ]
# Generated by Django 4.2.7 on 2024-10-15 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoAPT', '0010_notificacion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notificacion',
            old_name='id',
            new_name='idnoti',
        ),
    ]
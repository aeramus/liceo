# Generated by Django 3.2.9 on 2022-05-07 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alumnos',
            old_name='cursos',
            new_name='curso',
        ),
        migrations.RemoveField(
            model_name='alumnos',
            name='edad',
        ),
    ]

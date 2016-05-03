# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-10 17:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('especialidades', '0001_initial'),
        ('dependencias', '0001_initial'),
        ('grados', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=255)),
                ('apellidos', models.CharField(max_length=255)),
                ('cip', models.CharField(max_length=8)),
                ('dni', models.CharField(max_length=8)),
                ('dependencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Dependencia', to='dependencias.Dependencia')),
                ('especialidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='especialidades.Especialidad', verbose_name='Especialidad')),
                ('grado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Grado', to='grados.Grado')),
            ],
        ),
    ]
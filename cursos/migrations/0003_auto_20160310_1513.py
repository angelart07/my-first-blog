# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-10 20:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0002_auto_20160310_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='fecha_de_inicio',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='curso',
            name='fecha_de_termino',
            field=models.DateField(),
        ),
    ]

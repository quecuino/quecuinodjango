# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-09 21:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quecuino', '0008_auto_20190209_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recepta',
            name='imatge',
            field=models.ImageField(upload_to='media'),
        ),
    ]

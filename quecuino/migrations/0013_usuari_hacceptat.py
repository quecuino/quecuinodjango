# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-10 18:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quecuino', '0012_remove_usuari_sexe'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuari',
            name='hacceptat',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]

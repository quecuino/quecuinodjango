# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-08 20:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quecuino', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recepta',
            name='nom_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
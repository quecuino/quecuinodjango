# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse


# Create your models here.
class Usuari(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=15)
    cognom = models.CharField(max_length=50)
    datanaixament = models.DateField()
    sexe = models.CharField(max_length=6)
    email = models.EmailField()

    def __str__(self):
        return self.user.username

class Recepta(models.Model):
    nom_recepta = models.CharField(max_length=50)
    usuario = models.ForeignKey(Usuari, on_delete=models.CASCADE)
    data_creacio = models.DateField(default=datetime.now)
    descripcio = models.CharField(max_length=100, )
    ingredients = models.CharField(max_length=300)
    procediment = models.CharField(max_length=2000)
    vots = models.ManyToManyField(Usuari, related_name='likes',blank=True)
    imatge = models.CharField(max_length=50, default='')

    def votstotals(self):
        return self.vots.count()

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.id, self.nom_recepta])



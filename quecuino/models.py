# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Usuari(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=15, unique=True)
    cognom = models.CharField(max_length=50)
    datanaixament = models.DateField()
    email = models.EmailField()
    hacceptat = models.BooleanField()

    def __str__(self):
        return self.user.username

class Recepta(models.Model):
    nom_recepta = models.CharField(max_length=50)
    slug = models.SlugField(max_length=120)
    usuario = models.ForeignKey(Usuari, on_delete=models.CASCADE)
    data_creacio = models.DateField(default=datetime.now)
    descripcio = models.CharField(max_length=100, )
    ingredients = models.CharField(max_length=300)
    procediment = models.CharField(max_length=2000)
    vots = models.ManyToManyField(Usuari, related_name='likes',blank=True)
    votsenumero = models.IntegerField(default=0)
    imatge = models.ImageField(upload_to='static/Images')

    def save(self,*args, **kwargs):
        self.slug = slugify(self.nom_recepta)
        super(Recepta, self).save(*args, **kwargs)

    def votstotals(self):
        return self.vots.count()

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.id, self.slug])





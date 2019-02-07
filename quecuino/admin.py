# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Usuari, Recepta
# Register your models here.
admin.site.register(Usuari)
admin.site.register(Recepta)
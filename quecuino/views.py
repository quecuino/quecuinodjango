# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from quecuino.forms import FormUser, FormUserextendido, Formreceta
from quecuino.models import Usuari, Recepta
from datetime import date

# Create your views here.


def receta(request):
    print('entra')
    if request.method == 'POST':
        print('recetadentro')
        formre = Formreceta(request.POST)
        if formre.is_valid():
            print('recetamuydentro')
            Recepta.nom_user = formre.cleaned_data['']
            Recepta.data_creacio = date
            Recepta.vots = 0
            formre.save()
            return redirect('index')
    else:
        formre = Formreceta()
    context = {'formre': formre}
    return render(request, 'quecuino/crearreceta.html',context)


def index(request):
    recetas = Recepta.objects.all()
    usuari = Usuari.objects.all()
    return render(request, 'quecuino/index.html', {'recetas': recetas},{'usuari': usuari})


def register(request):
    if request.method == 'POST':
        form = FormUser(request.POST)
        profile_form = FormUserextendido(request.POST)
        print("post")

        if form.is_valid() and profile_form.is_valid():
            print("funciona")
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        print("esto no funciona")
        form = FormUser()
        profile_form = FormUserextendido()
    context = {'form': form, 'profile_form': profile_form}
    return render(request, 'registration/registro.html', context)

def logout(request):
    logout(request)
    return render(request, 'quecuino/index.html')
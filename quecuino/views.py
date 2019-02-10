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
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
# Create your views here.


def receta(request):
    print('entra')
    if request.method == 'POST':
        print('recetadentro')
        formre = Formreceta(request.POST,request.FILES)
        print formre.is_valid()
        if formre.is_valid():
            nueva_receta = formre.save(commit=False)
            usuario = Usuari.objects.get(id=request.user.id)
            nueva_receta.usuario = usuario
            nueva_receta.save()
            return redirect('index')
    else:
        formre = Formreceta()
    context = {'formre': formre}
    return render(request, 'quecuino/crearreceta.html', context)


def index(request):
    recetas = Recepta.objects.order_by()
    return render(request, 'quecuino/index.html', {'recetas': recetas}, )



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

def post_detail(request, id, slug):
    post = get_object_or_404(Recepta, id=id, slug=slug)
    is_liked = False
    if post.vots.filter(id=request.user.id).exists():
        is_liked = True
    context = {
        'post': post,
        'totallikes':post.votstotals(),
        'is_liked': is_liked
    }
    return render(request, 'quecuino/mostrarreceta.html',context)

def user_detail(request, usuario_id, usuario):
    recepta = Recepta.objects.filter(usuario_id=usuario_id)
    context = {
        'recepta':recepta
    }
    return render(request, 'quecuino/mostrarusuari.html',context)

def like_receta(request):
    post = get_object_or_404(Recepta, id=request.POST.get('post_id'))
    usuari = Usuari.objects.get(id=request.user.id)
    if post.vots.filter(id=request.user.id).exists():
        print 'im not doing my part'
        post.vots.remove(request.user.id)
        post.votsenumero = post.votstotals()
        post.save()
        is_liked = False

    else:
        print 'im doing my part'
        post.vots.add(usuari)
        post.votsenumero = post.votstotals()
        post.save()
        is_liked = True
    return HttpResponseRedirect(post.get_absolute_url())



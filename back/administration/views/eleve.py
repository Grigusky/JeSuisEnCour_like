# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.

def eleve_index(request):
    eleve = Eleve.object.all()
    context = {}
    return render(request, 'eleve_index.html', context)


def eleve_search(request):
    try:
        eleve = eleve.object.filter()
    except:
        eleve = eleve.object.all()
    context = {'eleve': eleve}
    return render(request, 'eleve_search.html', context)


def eleve_create(request):
    context = {}
    return render(request, 'eleve_create.html', context)


def eleve_create_act(request):
    return redirect()


def eleve_update(request):
    context = {}
    return render(request, 'eleve_update.html', context)


def eleve_update_act(request):
    return redirect()


def eleve_delete(request):
    context = {}
    return render(request, 'eleve_delete.html', context)


def eleve_delete_act(request):
    return redirect()

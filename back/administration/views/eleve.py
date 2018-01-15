# -*- coding: utf-8 -*-

from django.shortcuts import render

# Create your views here.

def eleve_index(request):
    context = {}
    return render(request, 'eleve_index.html', context)


def eleve_search(request):
    context = {}
    return render(request, 'eleve_search.html', context)


def eleve_create(request):
    context = {}
    return render(request, 'eleve_create.html', context)


def eleve_update(request):
    context = {}
    return render(request, 'eleve_update.html', context)


def eleve_delete(request):
    context = {}
    return render(request, 'eleve_delete.html', context)

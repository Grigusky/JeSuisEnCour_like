# -*- coding: utf-8 -*-

from django.shortcuts import render

# Create your views here.

def salle_index(request):
    salle = salle.objects.all()
    context = {}
    return render(request, 'salle_index.html', context)


def salle_search(request):
    try:
        salle = Salle.objects.filter()
    except:
        salle = Salle.objects.get()
    context = {}
    return render(request, 'salle_search.html', context)


def salle_create(request):
    context = {}
    return render(request, 'salle_create.html', context)


def salle_update(request):
    context = {}
    return render(request, 'salle_update.html', context)


def salle_delete(request):
    context = {}
    return render(request, 'salle_delete.html', context)

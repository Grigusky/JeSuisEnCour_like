# -*- coding: utf-8 -*-

from django.shortcuts import render

# Create your views here.

def specialite_index(request):
    specialite = Specialite.objects.all()
    context = {}
    return render(request, 'specialite_index.html', context)


def specialite_search(request):
    try:
        specialite = Specialite.objects.filter()
    except:
        specialite = Specialite.objects.all()
    context = {}
    return render(request, 'specialite_search.html', context)


def specialite_create(request):
    context = {}
    return render(request, 'specialite_create.html', context)


def specialite_update(request):
    context = {}
    return render(request, 'specialite_update.html', context)


def specialite_delete(request):
    context = {}
    return render(request, 'specialite_delete.html', context)

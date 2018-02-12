# -*- coding: utf-8 -*-

from django.shortcuts import render
from administration.models import *

# Create your views here.

def cours_index(request):
    cours = Cour.objects.all()
    context = {'cours': cours}
    return render(request, 'cours_index.html', context)


def cours_search(request):
    try:
        cours = Cours.objects.filter()
    except:
        cours = Cours.objects.all()
    context = {}
    return render(request, 'cours_search.html', context)


def cours_create(request):
    context = {}
    return render(request, 'cours_create.html', context)


def cours_update(request):
    context = {}
    return render(request, 'cours_update.html', context)


def cours_delete(request):
    context = {}
    return render(request, 'cours_delete.html', context)

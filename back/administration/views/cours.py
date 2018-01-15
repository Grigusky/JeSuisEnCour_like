# -*- coding: utf-8 -*-

from django.shortcuts import render

# Create your views here.

def cours_index(request):
    context = {}
    return render(request, 'cours_index.html', context)


def cours_search(request):
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

# -*- coding: utf-8 -*-

from django.shortcuts import render

# Create your views here.

def prof_index(request):
    context = {}
    return render(request, 'prof_index.html', context)


def prof_search(request):
    context = {}
    return render(request, 'prof_search.html', context)


def prof_create(request):
    context = {}
    return render(request, 'prof_create.html', context)


def prof_update(request):
    context = {}
    return render(request, 'prof_update.html', context)


def prof_delete(request):
    context = {}
    return render(request, 'prof_delete.html', context)

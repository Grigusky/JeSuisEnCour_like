# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Eleves(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.nom


class Specialite(models.Model):
    nom = models.CharField(max_length=50)
    classe = models.ForeignKey('Promotions',on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


class Specialite_Eleve(models.Model):
    eleve = models.ForeignKey('Eleves',on_delete=models.CASCADE)
    specialite = models.ForeignKey('Specialite',on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


class Absences_Eleve(models.Model):
    cours = models.ForeignKey('Cours',on_delete=models.CASCADE)
    eleve = models.ForeignKey('Eleves',on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return (self.cours + ' ' + self.eleve + ' ' + self.date)


class Prof(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return (self.nom + ' ' + self.prenom + ' ' + self.email)


class Prof_Promotion(models.Model):
    prof = models.ForeignKey('Prof',on_delete=models.CASCADE)
    promotion = models.ForeignKey('Promotions',on_delete=models.CASCADE)

    def __str__(self):
        return (self.prof.nom + ' ' + self.promotion.intitule )


class Absences_Prof(models.Model):
    cours = models.ForeignKey('Cours',on_delete=models.CASCADE)
    prof = models.ForeignKey('Prof',on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)
    justificatif = models.CharField(max_length=100)

    def __str__(self):
        return (self.cours + ' ' + self.prof + ' ' + self.date)


class Cours(models.Model):
    debut = models.DateField(auto_now=False, auto_now_add=False)
    fin = models.DateField(auto_now=False, auto_now_add=False)
    intitule = models.CharField(max_length=50)
    promotion = models.ForeignKey('Promotions',on_delete=models.CASCADE)

    def __str__(self):
        return (self.intitule + ':' + self.debut + '-' + self.fin)


class Promotions(models.Model):
    intitule = models.CharField(max_length=50)
    annee = models.CharField(max_length=25)

    def __str__(self):
        return (self.intitule + ' - ' + self.annee )

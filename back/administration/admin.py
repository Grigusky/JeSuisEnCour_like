# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Eleves)
admin.site.register(Specialite)
admin.site.register(Specialite_Eleve)
admin.site.register(Absences_Eleve)
admin.site.register(Prof)
admin.site.register(Prof_Promotion)
admin.site.register(Absences_Prof)
admin.site.register(Cours)
admin.site.register(Promotions)

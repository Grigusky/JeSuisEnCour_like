# coding: utf8

from django.conf.urls import include, url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import *


app_name = 'forti'
urlpatterns = [
        #index
        url(r'^$',views.index, name='index'),
        url(r'^eleve/index/$',views.eleve_index, name='index'),
        url(r'^prof/index/$',views.prof_index, name='index'),
        url(r'^cours/index/$',views.cours_index, name='index'),
        url(r'^salle/index/$',views.salle_index, name='index'),
        url(r'^specialite/index/$', views.specialite_index, name='index'),
        #search
        url(r'^eleve/search/$',views.eleve_search, name='search'),
        url(r'^prof/search/$',views.prof_search, name='search'),
        url(r'^cours/search/$',views.cours_search, name='search'),
        url(r'^salle/search/$',views.salle_search, name='search'),
        url(r'^specialite/search/$',views.specialite_search, name='search'),
        #create
        url(r'^eleve/create/$',views.eleve_create, name='create'),
        url(r'^prof/create/$',views.prof_create, name='create'),
        url(r'^cours/create/$',views.cours_create, name='create'),
        url(r'^salle/create/$',views.salle_create, name='create'),
        url(r'^specialite/create/$',views.specialite_create, name='create'),
        #update
        url(r'^eleve/update/$',views.eleve_update, name='update'),
        url(r'^prof/update/$',views.prof_update, name='update'),
        url(r'^cours/update/$',views.cours_update, name='update'),
        url(r'^salle/update/$',views.salle_update, name='update'),
        url(r'^specialite/update/$',views.specialite_update, name='update'),
        #delete
        url(r'^eleve/delete/$',views.eleve_delete, name='delete'),
        url(r'^prof/delete/$',views.prof_delete, name='delete'),
        url(r'^cours/delete/$',views.cours_delete, name='delete'),
        url(r'^salle/delete/$',views.salle_delete, name='delete'),
        url(r'^specialite/delete/$',views.specialite_delete, name='delete'),
        #api
        #list
        url(r'^api/eleve/list$', ElevesApi.as_view(), name="api eleve"),
        url(r'^api/specialite/list$', SpecialiteApi.as_view(), name="api eleve"),
        url(r'^api/specialite_eleve/list$', Specialite_EleveApi.as_view(), name="api eleve"),
        url(r'^api/absences_eleve/list$', Absences_EleveApi.as_view(), name="api eleve"),
        url(r'^api/prof/list$', ProfApi.as_view(), name="api eleve"),
        url(r'^api/prof_promotion/list$', Prof_PromotionApi.as_view(), name="api eleve"),
        url(r'^api/absences_prof/list$', Absences_ProfApi.as_view(), name="api eleve"),
        url(r'^api/cours/list$', CoursApi.as_view(), name="api eleve"),
        url(r'^api/promotions/list$', PromotionsApi.as_view(), name="api eleve"),
        # Create
        url(r'^api/eleve/create/$', ElevesCreateApi.as_view(), name="api create eleve"),
        url(r'^api/specialite/create/$', SpecialiteCreateApi.as_view(), name="api create eleve"),
        url(r'^api/specialite_eleve/create/$', Specialite_EleveCreateApi.as_view(), name="api create eleve"),
        url(r'^api/absences_eleve/create/$', Absences_EleveCreateApi.as_view(), name="api create eleve"),
        url(r'^api/prof/create/$', ProfCreateApi.as_view(), name="api create eleve"),
        url(r'^api/prof_promotion/create/$', Prof_PromotionCreateApi.as_view(), name="api create eleve"),
        url(r'^api/absences_prof/create/$', Absences_ProfCreateApi.as_view(), name="api create eleve"),
        url(r'^api/cours/create/$', CoursCreateApi.as_view(), name="api create eleve"),
        url(r'^api/promotions/create/$', PromotionsCreateApi.as_view(), name="api create eleve")
]

urlpatterns += staticfiles_urlpatterns()

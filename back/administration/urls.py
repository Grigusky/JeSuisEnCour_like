# coding: utf8
#v1.1
#v1.2
#v1.3 aka hardy zoophile
#v1.4 aka cochounou valentine
#v1.5 aka couscous merguez
#v1.6 aka malibu goldorak
#v1.7 aka kerosene underscore
#v1.8 aka wrecked papillon
#v1.9 aka asperger dentifrice
#v1.10 aka gianduja ‘rdin
#v1.11 aka suzuki master flash

from django.conf.urls import include, url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


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
]

urlpatterns += staticfiles_urlpatterns()

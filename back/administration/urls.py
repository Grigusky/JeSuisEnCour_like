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
        url(r'^api/promotions/create/$', PromotionsCreateApi.as_view(), name="api create eleve"),
        # Search
        url(r'^api/eleve/(?P<nom>[\w-]+)/$', ElevesSearchApi.as_view(), name="api eleve"),
        url(r'^api/specialite/(?P<nom>[\w-]+)/$', SpecialiteSearchApi.as_view(), name="api eleve"),
        url(r'^api/specialite_eleve/(?P<eleve>[\w-]+)/$', Specialite_EleveSearchApi.as_view(), name="api eleve"),
        url(r'^api/absences_eleve/(?P<eleve>[\w-]+)/$', Absences_EleveSearchApi.as_view(), name="api eleve"),
        url(r'^api/prof/(?P<nom>[\w-]+)/$', ProfSearchApi.as_view(), name="api eleve"),
        url(r'^api/prof_promotion/(?P<prof>[\w-]+)/$', Prof_PromotionSearchApi.as_view(), name="api eleve"),
        url(r'^api/absences_prof/(?P<prof>[\w-]+)/$', Absences_ProfSearchApi.as_view(), name="api eleve"),
        url(r'^api/cours/(?P<intitule>[\w-]+)/$', CoursSearchApi.as_view(), name="api eleve"),
        url(r'^api/promotions/(?P<name>[\w-]+)/$', PromotionsSearchApi.as_view(), name="api eleve"),
        # Update
        url(r'^api/eleve/(?P<nom>[\w-]+)/update/$', ElevesUpdateApi.as_view(), name="api eleve"),
        url(r'^api/specialite/(?P<nom>[\w-]+)/update/$', SpecialiteUpdateApi.as_view(), name="api eleve"),
        url(r'^api/specialite_eleve/(?P<eleve>[\w-]+)/update/$', Specialite_EleveUpdateApi.as_view(), name="api eleve"),
        url(r'^api/absences_eleve/(?P<eleve>[\w-]+)/update/$', Absences_EleveUpdateApi.as_view(), name="api eleve"),
        url(r'^api/prof/(?P<nom>[\w-]+)/update/$', ProfUpdateApi.as_view(), name="api eleve"),
        url(r'^api/prof_promotion/(?P<prof>[\w-]+)/update/$', Prof_PromotionUpdateApi.as_view(), name="api eleve"),
        url(r'^api/absences_prof/(?P<prof>[\w-]+)/update/$', Absences_ProfUpdateApi.as_view(), name="api eleve"),
        url(r'^api/cours/(?P<intitule>[\w-]+)/update/$', CoursUpdateApi.as_view(), name="api eleve"),
        url(r'^api/promotions/(?P<name>[\w-]+)/update/$', PromotionsUpdateApi.as_view(), name="api eleve"),
        # Delete
        url(r'^api/eleve/(?P<nom>[\w-]+)/delete/$', ElevesDeleteApi.as_view(), name="api eleve"),
        url(r'^api/specialite/(?P<nom>[\w-]+)/delete/$', SpecialiteDeleteApi.as_view(), name="api eleve"),
        url(r'^api/specialite_eleve/(?P<eleve>[\w-]+)/delete/$', Specialite_EleveDeleteApi.as_view(), name="api eleve"),
        url(r'^api/absences_eleve/(?P<eleve>[\w-]+)/delete/$', Absences_EleveDeleteApi.as_view(), name="api eleve"),
        url(r'^api/prof/(?P<nom>[\w-]+)/delete/$', ProfDeleteApi.as_view(), name="api eleve"),
        url(r'^api/prof_promotion/(?P<prof>[\w-]+)/delete/$', Prof_PromotionDeleteApi.as_view(), name="api eleve"),
        url(r'^api/absences_prof/(?P<prof>[\w-]+)/delete/$', Absences_ProfDeleteApi.as_view(), name="api eleve"),
        url(r'^api/cours/(?P<intitule>[\w-]+)/delete/$', CoursDeleteApi.as_view(), name="api eleve"),
        url(r'^api/promotions/(?P<name>[\w-]+)/delete/$', PromotionsDeleteApi.as_view(), name="api eleve"),
]

urlpatterns += staticfiles_urlpatterns()

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
        url(r'^$',views.index, name='index'),
]

urlpatterns += staticfiles_urlpatterns()


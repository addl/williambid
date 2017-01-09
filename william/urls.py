from django.conf.urls import patterns, include, url
from django.contrib import admin

from back_office.views import mostrar_paquetes_de_bids
from williambid.views import home_page, pujar, obtener_subasta_json, autenticar, salir, change_language, search, \
    acerca_de, terminos, comprar_paquetes_de_bids, business_opportunity

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'william.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^$', home_page),
                       url(r'^user/(\w+)$', home_page),
                       url(r'^lang/(\w+)$', change_language),
                       url(r'^search/$', search),
                       url(r'^about/$', acerca_de),
                       url(r'^terms/$', terminos),
                       url(r'^business-opportunity/$', business_opportunity),
                       url(r'^xhr/data/subasta/(\d+)/$', obtener_subasta_json),
                       url(r'^xhr/pujar/(\d+)/$', pujar),
                       url(r'^paquetes-bid/comprar$', mostrar_paquetes_de_bids),
                       url(r'^paquetes-bid/comprar/(\d+)/$', comprar_paquetes_de_bids),
                       url(r'^usuarios/', include('back_office.urls')),
                       url(r'^autenticar/$', autenticar),
                       url(r'^salir/$', salir),
                       url(r'^admin/', include(admin.site.urls)),
                       )

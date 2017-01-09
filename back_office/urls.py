from django.conf.urls import patterns, include, url
from back_office.views import register, mostrar_backoffice, invitar_usuario, mostrar_red, mostrar_banco, \
    mostrar_subastas, \
    cuentas_de_usuario, mostrar_administracion, mostrar_retos, mostrar_mensajes, mostrar_herramientas, enviar_mensaje, \
    retos_de_usuarios, estado_retos_de_usuarios, \
    inscribir_usuario_reto, cargar_red_de_usuario, mostrar_paquetes_de_bids, estado_de_usuario_en_planes, user_profile, \
    show_user_profile, edit_user_profile, show_auto_pujas, delete_auto_puja, edit_auto_puja, show_cart, \
    improve_membership, \
    shopping_cart_payment, paypal_return_endpoint, delete_item_from_cart, paypal_cancel_endpoint
from williambid.views import obtener_subasta_json, pujar

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'william.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^registro/$', register),
                       url(r'^back-office/$', mostrar_backoffice),
                       # url(r'^back-office/administracion/$', mostrar_administracion),
                       url(r'^back-office/administracion/profile/show/$', show_user_profile),
                       url(r'^back-office/administracion/profile/edit/$', edit_user_profile),
                       url(r'^back-office/administracion/profile/better/membership/$', improve_membership),
                       url(r'^back-office/administracion/red/$', mostrar_red),
                       url(r'^back-office/administracion/banco/$', mostrar_banco),
                       url(r'^back-office/administracion/subastas/$', mostrar_subastas),
                       url(r'^back-office/administracion/retos/$', mostrar_retos),
                       url(r'^back-office/administracion/autopujas/$', show_auto_pujas),
                       url(r'^back-office/administracion/shopping-cart/$', show_cart),
                       url(r'^back-office/administracion/shopping-cart/delete/$', delete_item_from_cart),
                       url(r'^back-office/administracion/shopping-cart/payment/$', shopping_cart_payment),
                       # this URL is manage by django-paypal app
                       url(r'^paypal/', include('paypal.standard.ipn.urls')),
                       url(r'^back-office/administracion/payment/return/$', paypal_return_endpoint),
                       url(r'^back-office/administracion/payment/cancelation/$', paypal_cancel_endpoint),
                       url(r'^back-office/administracion/autopujas/delete/$', delete_auto_puja),
                       url(r'^back-office/administracion/autopujas/add/$', edit_auto_puja),
                       url(r'^back-office/administracion/autopujas/edit/$', edit_auto_puja),
                       url(r'^back-office/administracion/mensajes/$', mostrar_mensajes),
                       url(r'^back-office/administracion/mensajes/send/$', enviar_mensaje),
                       url(r'^back-office/administracion/ads$', mostrar_herramientas),
                       url(r'^back-office/administracion/paquetes-bid$', mostrar_paquetes_de_bids),
                       url(r'^invitacion/$', invitar_usuario),
                       url(r'^invitacion/(\w+)/$', register),
                       # peticiones AJAX
                       url(r'^back-office/xhr/data/cuenta/$', cuentas_de_usuario),
                       url(r'^back-office/xhr/data/planes_estado/$', estado_de_usuario_en_planes),
                       url(r'^back-office/xhr/data/retos/$', retos_de_usuarios),
                       url(r'^back-office/xhr/data/retos/estado/$', estado_retos_de_usuarios),
                       url(r'^back-office/xhr/data/retos/inscripcion/$', inscribir_usuario_reto),
                       url(r'^back-office/xhr/data/red/red/$', cargar_red_de_usuario),
                       url(r'^back-office/xhr/data/profile/$', user_profile),
                       # estas 2 son las mismas reglas que para el index de williambid
                       url(r'^back-office/administracion/subastas/xhr/data/subasta/(\d+)/$', obtener_subasta_json),
                       url(r'^back-office/administracion/subastas/xhr/pujar/(\d+)/$', pujar),
                       )

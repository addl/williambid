from itertools import chain
import json

import datetime

from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect, HttpResponse, HttpResponseForbidden
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.models import User
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm

from back_office.banco import obtener_factura_total_de_usuario
from back_office.forms import RegistrationForm
from back_office.models import Invitacion, Reto, EstadoRetoUsuario, Mensaje, AdvertisementTool, PlanCompensacion, \
    WilliamPaypalTransaction
from back_office.my_math_module import msum
from back_office.tasks import obtener_primera_generacion_de, registrar_usuario_nuevo_a_planes_de_compensacion
from back_office.util import encriptar_usuario, generar_url_para_usuario_encriptado, desencriptar_nombre_de_usuario, \
    obtener_usuario_desde_nombre_hexadecimal, obtener_objeto_json, obtener_plantilla_de_reto, \
    determinar_si_usuario_puede_cobrar_plan, construir_mapa_de_estado_en_plan, es_usuario_x_ancestro_de_usuario_y
from williambid.models import Subasta, PaqueteBid, AutoPuja, Articulo, SubastaVendida, Venta
from williambid.service_layer import obtener_subastas_vendidas_recientemente, obtener_subastas_pujando, \
    obtener_subastas_vendidas
from back_office.back_office_service_layer import esta_usuario_participando_en_reto, \
    inscribir_usuario_en_reto, es_usuario_ganador_de_reto
from williambid.utils import registrar_usuario, obtener_user_formato_json, actualizar_perfil_de_usuario
import logging

PAYPAL_WILLIAM_ADDRESS = "receiver_email@example.com"
log = logging.getLogger(__name__)


# Create your views here.
def common_data(request, dicts=None):
    proximas_subastas_lista = Subasta.objects.filter(estado=Subasta.WAITING)
    ultimas_subastas_lista = list(obtener_subastas_vendidas())[:10]
    # el RequestContext se utiliza para los form y validar el csrf token
    data = RequestContext(request)
    # para recuperar esta lista en las templates es simplemente el nombre "ultimas_subastas"
    data.dicts.append({'ultimas_subastas': ultimas_subastas_lista, })
    data.dicts.append({'proximas_subastas': proximas_subastas_lista, })
    # balance genarl del usuario actual
    factura_total = obtener_factura_total_de_usuario(request.user)
    data.dicts.append({'general_balance': factura_total, })
    # informacion del usuario
    user = request.user
    new_mesgs = Mensaje.objects.filter(leido=False, para_usuario_id=user.id)
    limite_fecha_de_membresia = user.perfilusuario.fecha_obtuvo_membresia + datetime.timedelta(days=30)
    # countdown_membresia = datetime.datetime.now() - limite_fecha_de_membresia
    user_info_dict = {'cantidad_usuarios_en_red': user.perfilusuario.hijos.count(),
                      'cantidad_de_bids': user.perfilusuario.cantidad_de_bids,
                      'cantidad_de_puntos': user.perfilusuario.cantidad_de_puntos,
                      'membresia_fecha_limite': limite_fecha_de_membresia,
                      'new_msgs': len(new_mesgs),
                      'shopping_cart_count': len(user.shoppinggcart.subastavendida_set.all()),
                      'share_url': "http://%s/user/%s" % (request.get_host(), request.user.username)
                      }
    data.dicts.append({'user_info': user_info_dict})
    # agregamos al request los demas datos que se pasaron en dicts
    if dicts is not None:
        for d in dicts:
            data.dicts.append(d)
    print 'returning data ', data.dicts
    return data


@login_required(login_url='/')
def mostrar_backoffice(request):
    # result = get_arbol_general.delay()
    # print "Result fetch data: %s" % result.get()
    usuario = request.user
    print 'Tipo de usuario %s' % type(usuario)
    subastas = chain(obtener_subastas_vendidas_recientemente(), obtener_subastas_pujando())
    return render_to_response('index_back_office.html', common_data(request, [{'subastas': subastas}]))


@login_required(login_url='/')
def mostrar_administracion(request):
    return render_to_response('administracion/administracion.html', common_data(request))


@login_required(login_url='/')
def mostrar_red(request):
    return render_to_response('administracion/red_miembros.html', common_data(request))


@login_required(login_url='/')
def show_user_profile(request):
    return render_to_response('administracion/profile-show.html', common_data(request))


@login_required(login_url='/')
def edit_user_profile(request):
    if request.method == 'GET':
        return render_to_response('administracion/profile-edit.html', common_data(request))
    else:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            actualizar_perfil_de_usuario(form, request.user)
            return HttpResponseRedirect('/usuarios/back-office')
        else:
            return render_to_response('administracion/profile-edit.html', {'form': form}, RequestContext(request))


@login_required(login_url='/')
def improve_membership(request):
    return render_to_response('administracion/improve_membership.html', common_data(request))


@login_required(login_url='/')
def mostrar_banco(request):
    return render_to_response('administracion/bank.html', common_data(request))


@login_required(login_url='/')
def mostrar_subastas(request):
    subastas = chain(obtener_subastas_vendidas_recientemente(), obtener_subastas_pujando())
    return render_to_response('administracion/auctons.html', common_data(request, [{'subastas': subastas}]))


@login_required(login_url='/')
def mostrar_retos(request):
    return render_to_response('administracion/retos.html', common_data(request))


@login_required(login_url='/')
def show_cart(request):
    return render_to_response('administracion/shopingcart.html', common_data(request))


@login_required(login_url='/')
def delete_item_from_cart(request):
    if 'subasta_id' in request.GET:
        subasta_vendida = SubastaVendida.objects.get(id=request.GET['subasta_id'])
        # el articulo que se vendio se adiciona uno en cantidad
        if subasta_vendida.subasta.contenido.articulo:
            articulo = subasta_vendida.subasta.contenido.articulo
            articulo.cantidad_de_articulos = articulo.cantidad_de_articulos + 1
            articulo.save(force_update=True)
        subasta_vendida.delete()
    return render_to_response('administracion/shopingcart.html', common_data(request))


@csrf_exempt
@login_required(login_url='/')
def paypal_return_endpoint(request):
    log.info("Returning from paypal")
    log.info("The request POST %s" % request.POST)


@login_required(login_url='/')
def paypal_cancel_endpoint(request):
    log.info("Cancel receiving from paypal")
    log.info("The request POST-GET %s-%s" % (request.POST, request.GET))


# we need to connect some signal to verify the status in the transaction
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received, invalid_ipn_received


def show_me_the_money(sender, **kwargs):
    try:
        log.info('Show me the money, receiving sender:%s and kwargs:%s' % (sender, kwargs))
        ipn_obj = sender
        if ipn_obj.payment_status == ST_PP_COMPLETED:
            # Check that the receiver email is the same we previously
            if ipn_obj.receiver_email != PAYPAL_WILLIAM_ADDRESS:
                # Not a valid payment
                log.error('Aborting confirm sales, DIFFERENT EMAILS- receiver_email:%s != paypal_setting:%s') % (
                ipn_obj.receiver_email, PAYPAL_WILLIAM_ADDRESS)
                return
            # ALSO we need to check the amount
            # Undertake some action depending upon `ipn_obj`.
            william_txn_id = int(ipn_obj.custom)
            william_txn = WilliamPaypalTransaction.objects.get(id=william_txn_id)
            if float(ipn_obj.amount) != float(william_txn.amount):
                log.error('Aborting confirm sales, DIFFERENT AMOUNTS %s != %s' % (ipn_obj.amount, william_txn.amount))
                return
            # at this point everything is OK, so we need to confirm ventas
            log.info('Payment CONFIRMED, confirming sales and clear user cart')
            user_cart = william_txn.user.shoppinggcart
            for subasta_vendida in user_cart.subastavendida_set:
                venta = Venta.objects.filter(subasta=subasta_vendida).first()
                # confirmamos la venta relacionada a esta subasta vendida
                venta.confirmada = True
                venta.fecha_confirmacion = datetime.datetime.now()
                venta.save(force_update=True)
                # eliminamos la subasta del carrito del usuario
                subasta_vendida.shoppinggcart = None
                subasta_vendida.save(force_update=True)
        else:
            log.error("The payment status isn/t completed: ipn_obj.payment_status == ST_PP_COMPLETED")
    except Exception, e:
        log.error("Error on show_me_the_money: rason is: %s" % e)


valid_ipn_received.connect(show_me_the_money)


def invalid_transaction(**kwargs):
    log.error("INVALID IPN, kwarggs is %s" % kwargs)
    log.error("INVALID IPN")
    log.error("INVALID IPN")


invalid_ipn_received.connect(invalid_transaction)


@login_required(login_url='/')
def shopping_cart_payment(request):
    # calculate the whole price
    notify_url = "https://%s%s" % (request.get_host(), reverse('paypal-ipn'))
    return_url = "https://%s/usuarios/back-office/administracion/payment/return/" % request.get_host()
    cancel_url = "https://%s/usuarios/back-office/administracion/payment/cancelation/" % request.get_host()
    amounts = []
    for subasta_vendida in request.user.shoppinggcart.subastavendida_set.all():
        amounts.append(subasta_vendida.subasta.precio_actual)
    total_amount = msum(amounts)
    # store the amount in WilliamPaypalTransaction
    william_txn = WilliamPaypalTransaction.objects.create(user=request.user, amount=total_amount)
    # What you want the button to do.
    paypal_dict = {
        "business": PAYPAL_WILLIAM_ADDRESS,
        "amount": str(total_amount),
        "item_name": "name of the item",
        "invoice": "unique-invoice-id",
        "notify_url": notify_url,
        "return_url": return_url,
        "cancel_return": cancel_url,
        "custom": str(william_txn.id),  # Custom command to correlate to some function later (optional)
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render_to_response('administracion/pago.html', common_data(request, [{'form': form}]))


@login_required(login_url='/')
def show_auto_pujas(request):
    user = request.user
    autopujas = AutoPuja.objects.filter(usuario=user).all()
    return render_to_response('administracion/autopujas.html',
                              common_data(request, [{'autopujas': autopujas}]))


@login_required(login_url='/')
def delete_auto_puja(request):
    user = request.user
    autopuja = AutoPuja.objects.filter(usuario=user, id=request.GET['autopuja_id'])
    if autopuja:
        autopuja.delete()
    return redirect("/usuarios/back-office/administracion/autopujas")


@login_required(login_url='/')
def edit_auto_puja(request):
    user = request.user
    if request.method == "GET":
        autopuja = None
        if 'autopuja_id' in request.GET:
            autopuja = AutoPuja.objects.filter(usuario=user, id=request.GET['autopuja_id']).first()
        return render_to_response('administracion/edit_auto_puja.html',
                                  common_data(request, [{'autopuja': autopuja, 'articles': Articulo.objects.all()}]))
    elif request.method == 'POST':
        cant_bids = request.POST['cantidad_pujas']
        article_id = request.POST['article_id']
        if 'autopuja_id' in request.POST:
            autopuja = AutoPuja.objects.filter(usuario=user, id=request.POST['autopuja_id']).first()
            autopuja.cantidad_pujas = cant_bids
            autopuja.articulo = Articulo.objects.get(id=article_id)
            autopuja.save(force_update=True)
        else:
            autopuja = AutoPuja(cantidad_pujas=cant_bids, usuario=user, articulo=Articulo.objects.get(id=article_id))
            autopuja.save(force_insert=True)
        return redirect("/usuarios/back-office/administracion/autopujas")


@login_required(login_url='/')
def mostrar_mensajes(request):
    user = request.user
    task = obtener_primera_generacion_de.delay(user.id)
    user_red = task.get()
    if not user.is_superuser:
        user_red.append(User.objects.get(id=user.perfilusuario.padre_id))
    # user_red = []
    mensajes = Mensaje.objects.filter(para_usuario=user)
    mensajes_per_user = dict()
    for msg in mensajes:
        remitente = msg.de_usuario
        if remitente.username not in mensajes_per_user:
            mensajes_per_user[remitente.username] = list()
        mensajes_per_user[remitente.username].append(msg)
        msg.leido = True
        msg.save(force_update=True)
    return render_to_response('administracion/messages.html',
                              common_data(request, [{'mensajes': mensajes_per_user, 'user_red': user_red}]))


@login_required(login_url='/')
def enviar_mensaje(request):
    user_id = request.POST['user_to']
    to_user = User.objects.get(username=user_id)
    if to_user is None:
        return redirect("/usuarios/back-office/administracion/mensajes/")

    message = request.POST['message']
    Mensaje.objects.create(de_usuario=request.user, para_usuario=to_user, mensaje=message)
    print "Sending message to %s, message is %s" % (to_user, message)
    return redirect("/usuarios/back-office/administracion/mensajes/")


@login_required(login_url='/')
def mostrar_herramientas(request):
    tools = AdvertisementTool.objects.all()
    return render_to_response('administracion/publicidad.html', common_data(request, [{'herramientas': tools}]))


@login_required(login_url='/')
def mostrar_paquetes_de_bids(request):
    paquetes = PaqueteBid.objects.all()
    return render_to_response('administracion/bids_packages.html', common_data(request, [{'paquetes': paquetes}]))


@login_required(login_url='/')
def invitar_usuario(request):
    nombre_usuario = request.user.username
    to_user = request.POST['to_user']
    to_email = request.POST['to_email']
    usuario_encriptado = encriptar_usuario(nombre_usuario)
    url = generar_url_para_usuario_encriptado(usuario_encriptado, request)
    # guardar la invitacion en base de datos
    invitacion = Invitacion(de_usuario=request.user, para=to_user, para_correo=to_email, url=url)
    invitacion.save()
    # enviar correo al usuario invitado
    return mostrar_backoffice(request)


@login_required(login_url='/')
def estado_de_usuario_en_planes(request):
    usuario = request.user
    planes = PlanCompensacion.objects.all()
    estado_user_en_planes = {}
    for plan in planes:
        estado = {}
        estado['descripcion'] = plan.descripcion
        estado['estado'] = determinar_si_usuario_puede_cobrar_plan(usuario, plan)
        # creamos un estado por cada requisito; sera una lista de 3 posiciones:
        # la primera posicion sera, -1 si esta por debajo, 0 si no se mide, 1 si esta por encima o lo cumple
        construir_mapa_de_estado_en_plan(usuario, plan, estado)
        estado_user_en_planes[plan.num_plan] = estado
    return HttpResponse(json.dumps({'estado_planes': estado_user_en_planes}, ensure_ascii=False),
                        content_type='application/json')


@login_required(login_url='/')
def retos_de_usuarios(request):
    usuario = request.user
    lista_de_retos = Reto.objects.filter(terminado=False)
    # para crea nuestro propio objeto json, sera cada value dentro del map
    lista_retos_json = []
    for reto in lista_de_retos:
        reto_json = dict()
        reto_json['reto'] = obtener_objeto_json(reto)
        reto_json['participa'] = esta_usuario_participando_en_reto(usuario, reto)
        reto_json['ganador'] = es_usuario_ganador_de_reto(usuario, reto)
        reto_json['descripcion'] = obtener_plantilla_de_reto(reto)
        lista_retos_json.append(reto_json)
        print "Object to JSON is %s" % reto_json
    return HttpResponse(json.dumps({'retos': lista_retos_json}, ensure_ascii=False), content_type='application/json')


@login_required(login_url='/')
def estado_retos_de_usuarios(request):
    usuario = request.user
    lista_estado_retos = EstadoRetoUsuario.objects.filter(usuario=usuario)
    lista_retos_json = serializers.serialize('json', lista_estado_retos)
    return HttpResponse(json.dumps({'retos_usuarios': lista_retos_json}, ensure_ascii=False),
                        content_type='application/json')


@login_required(login_url='/')
def inscribir_usuario_reto(request):
    usuario = request.user
    print 'parameters %s ' % request.GET
    reto_id = request.GET['reto_id']
    inscribir_usuario_en_reto(usuario, reto_id)
    return HttpResponse(json.dumps({'status': 200}, ensure_ascii=False), content_type='application/json')


@login_required(login_url='/')
def cuentas_de_usuario(request):
    # hay ver como ponemos el manager plan en ejecucion
    user = request.user
    lista_cuentas = user.bancousuario_set.all()
    cuentas_json = serializers.serialize('json', lista_cuentas)
    return HttpResponse(json.dumps({'cuentas': cuentas_json}, ensure_ascii=False), content_type='application/json')


@login_required(login_url='/')
def cargar_red_de_usuario(request):
    user = request.user
    if 'username' in request.GET:
        user = User.objects.get(username=request.GET['username'])
    if user.id != request.user.id:
        if not es_usuario_x_ancestro_de_usuario_y(request.user, user):
            return HttpResponseForbidden()
    result = obtener_primera_generacion_de.delay(user.id)
    first_generation = result.get()
    # first_generation = []
    usuarios_in_json = []
    for user in first_generation:
        usuarios_in_json.append(obtener_user_formato_json(user))

    return HttpResponse(json.dumps({'first_generation': usuarios_in_json}, ensure_ascii=False),
                        content_type='application/json')


@login_required(login_url='/')
def user_profile(request):
    username = request.GET['username']
    user_json = obtener_user_formato_json(User.objects.filter(username=username).first())

    return HttpResponse(json.dumps({'user_profile': user_json}, ensure_ascii=False),
                        content_type='application/json')


def register(request, from_usuario=None):
    print "Inside register view... from usuario is %s" % from_usuario
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            try:
                # para dar simplicidad a esta vista, hicimos una funcion util
                # si fue una invitacion agregar el usuario a los planes de compensacion
                user_from = None
                if 'invitacion' in request.POST:
                    user_from = obtener_usuario_desde_nombre_hexadecimal(request.POST['invitacion'])
                if request.session.has_key('sharer_parent'):
                    sharer_parent = request.session.get('sharer_parent')
                    user_from = User.objects.get(username=sharer_parent)
                invited_user = registrar_usuario(form, user_from)
                # hay q registrar el usuario nuevo a los planes de compensacion
                registrar_usuario_nuevo_a_planes_de_compensacion.delay(invited_user, user_from)
            except Exception, e:
                print e
                form.add_error(None, "No podemos atender su solicitud en este momento")
                return render_to_response('register.html', {'form': form, 'invitacion': from_usuario},
                                          RequestContext(request))
            return HttpResponseRedirect('/usuarios/back-office')
        # si el formulario no reune los requisitos lo mostramos de nuevo
        else:
            return render_to_response('register.html', {'form': form, 'invitacion': from_usuario},
                                      RequestContext(request))
    else:
        form = RegistrationForm
        return render_to_response('register.html', {'form': form, 'invitacion': from_usuario}, RequestContext(request))

import os
from itertools import chain
import json
import datetime
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.gis.db.backends import mysql
from django.core import serializers
from django.core.urlresolvers import reverse
from django.http.response import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, render_to_response

from django.template.context import RequestContext
from paypal.standard.forms import PayPalPaymentsForm

from back_office.models import PlanCompensacion, WilliamPaypalTransaction, PackageTransaction
from back_office.my_math_module import msum
from williambid.models import Subasta, PaqueteBid
from williambid.robot_manager import RobotManager
from williambid.service_layer import pujar_subasta, obtener_subastas_pujando, obtener_subastas_vendidas_recientemente, \
    obtener_subastas_vendidas, buscar_subastas
from williambid.tasks import asignar_robots_a_subastas
from williambid.utils import obtener_subasta_formato_json, OnlineUsers, findPlansFileDescriptorByLocale
# language stuff
from django.utils import translation
from django.conf import settings


# Create your views here.
def common_data(request, dicts=None):
    # el RequestContext se utiliza para los form y validar el csrf token
    data = RequestContext(request)
    # para recuperar esta lista en las templates es simplemente el nombre "ultimas_subastas"
    ultimas_subastas_lista = list(obtener_subastas_vendidas())[:5]
    data.dicts.append({'ultimas_subastas': ultimas_subastas_lista, })
    proximas_subastas_lista = list(Subasta.objects.filter(estado=Subasta.WAITING))[:5]
    data.dicts.append({'proximas_subastas': proximas_subastas_lista, })
    online_users = OnlineUsers.obtener_usuarios_online()
    data.dicts.append({'usuarios_en_linea': online_users})
    paquetes_de_pujas = PaqueteBid.objects.all()
    data.dicts.append({'paquetes_de_pujas': paquetes_de_pujas})
    # agregamos al request los demas datos que se pasaron en el parametro dicts
    if dicts is not None:
        for d in dicts:
            data.dicts.append(d)
    print 'returning data ', data.dicts
    return data


def change_language(request, lang):
    print 'setting language', lang
    translation.activate(lang)
    response = HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang)
    return response


def search(request):
    language = translation.get_language()
    querysearch = request.GET['querysearch']
    results_subastas = buscar_subastas(querysearch, language)
    print 'Searching by %s. Current language is %s, results %s.' % (querysearch, language, results_subastas)
    return render_to_response('search_results.html', common_data(request, [{'subastas': results_subastas}]))


def acerca_de(request):
    return render_to_response('about.html', common_data(request, []))


def terminos(request):
    return render_to_response('terms.html', common_data(request, []))


def business_opportunity(request):
    return render_to_response('business_opportunity.html', common_data(request, [{'plans': PlanCompensacion.objects.all()}]))


def dispose_plans_descriptor_file(request):
    my_file = findPlansFileDescriptorByLocale(request.LANGUAGE_CODE)
    response = HttpResponse(my_file.read(), content_type='application/octet-stream')
    # print 'attaching ', download_file
    response['Content-Disposition'] = 'attachment; filename="%s"' % os.path.split(my_file.name)[1]
    # response['Content-Disposition'] = 'attachment; filename="%s"' % my_file.name
    # response['X-Sendfile'] = smart_str(process.file_results)
    return response


def home_page(request, username=None):
    if username:
        print "Found invitation...."
        # until the user close the browser I will store his prospective parent
        request.session.set_expiry(0)
        request.session['sharer_parent'] = username
    print 'path del request %s' % request.get_full_path()
    subastas = chain(obtener_subastas_vendidas_recientemente(), obtener_subastas_pujando())
    return render_to_response('index.html', common_data(request, [{'subastas': subastas}]))


from django.contrib.auth import login


def autenticar(request):
    user = request.POST['user']
    password = request.POST['password']
    usuario = authenticate(username=user, password=password)
    if usuario:
        login(request, usuario)
        return HttpResponseRedirect('/usuarios/back-office/', common_data(request))
    else:
        return render_to_response('index.html', common_data(request, [{"errors": "Credenciales incorrectas"}]))


def salir(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def pujar(request, subasta_id):
    user = request.user
    # puede que haya que verificar si un usuario puede pujar en esta subasta
    # aqui y en las autopujas del sincronizador
    if not user.perfilusuario.cantidad_de_bids > 0:
        return HttpResponseForbidden()
    print 'Pujando a la subasta %s' % subasta_id
    if subasta_id is None:
        return
    # ir a la capa de servicio y pujar contra base de datos
    band = pujar_subasta(subasta_id, request.user)
    if band:
        # quitarle un bid al usuario, NO a los robots
        user.perfilusuario.cantidad_de_bids = user.perfilusuario.cantidad_de_bids - 1
        user.perfilusuario.save(force_update=True)
        # poner al tanto al sincronizador que asigna robots a la subasta
        task = asignar_robots_a_subastas.delay(subasta_id)
    one_subasta_to_json = obtener_subasta_formato_json(Subasta.objects.get(id=subasta_id))
    return HttpResponse(json.dumps({'status': '200', 'subasta': one_subasta_to_json},
                                   ensure_ascii=False), content_type='text/html')


def obtener_subasta_json(request, subasta_id):
    subasta = Subasta.objects.get(id=subasta_id)
    # comparar precios
    precio_bd = round(subasta.precio_actual, 2)
    precio_user = request.GET['precio_actual']
    precio_user = str(precio_user).replace(",", ".")
    actualizar_subasta_en_dom = float(precio_bd) > float(precio_user)
    one_subasta_to_json = obtener_subasta_formato_json(Subasta.objects.get(id=subasta_id))
    return HttpResponse(
        json.dumps({'status': '200', 'actualizar': actualizar_subasta_en_dom, 'subasta': one_subasta_to_json},
                   ensure_ascii=False), content_type='text/html')


@login_required(login_url='/')
def comprar_paquetes_de_bids(request, paquete_id):
    pkte = PaqueteBid.objects.get(id=paquete_id)
    # calculate the whole price
    notify_url = "https://%s%s" % (request.get_host(), reverse('paypal-ipn'))
    return_url = "https://%s/usuarios/back-office/administracion/payment/return/" % request.get_host()
    cancel_url = "https://%s/usuarios/back-office/administracion/payment/cancelation/" % request.get_host()
    amounts = []
    for subasta_vendida in request.user.shoppinggcart.subastavendida_set.all():
        amounts.append(subasta_vendida.subasta.precio_actual)
    total_amount = pkte.precio
    # store the amount in WilliamPaypalTransaction
    william_txn = PackageTransaction.objects.create(user=request.user, amount=total_amount, pkt_id=pkte.id)
    # What you want the button to do.
    paypal_dict = {
        "business": settings.PAYPAL_WILLIAM_ADDRESS,
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

    # return render_to_response('administracion/pago.html', common_data(request, [{'form': form}]))
    return render_to_response('comprar_paquete.html', common_data(request, [{'paquete': pkte, 'form': form}]))


def mostrar_paquetes_de_bids(request):
    paquetes_bids = PaqueteBid.objects.all()
    return render_to_response('all_packages.html', common_data(request, [{'paquetes_bids': paquetes_bids}]))

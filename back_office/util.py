import json
import random
from django.contrib.auth.models import User
from django.contrib.sites.models import get_current_site
from django.core import serializers

from back_office.banco import obtener_factura_total_de_usuario
from back_office.models import UserXDeliveredProfit
from back_office.planes.utils import obtener_lista_de_usuarios
from williambid.models import Venta, VentaPaqueteBid, VentaArticulo

__author__ = 'bryan'

from simplecrypt import encrypt, decrypt
from binascii import hexlify, unhexlify

CLAVE = 'secreta'


def generar_url_para_usuario_encriptado(usuario_encriptado, request):
    # usamos la funcion hexlify para mostrar caracteres en vez de codigo ascii
    usuario_caracteres = hexlify(usuario_encriptado)
    url = "http://%s/usuarios/invitacion/%s" % (get_current_site(request), usuario_caracteres)
    return url


def obtener_usuarios_mayor_a_basic():
    usuarios = obtener_lista_de_usuarios(exclude_admin=False)
    # adicionamos por default el admin
    usuarios_basic = []
    # solo los usuarios mayor que basic pueden cobrar este plan
    for user in usuarios:
        if user.perfilusuario.membresia.tipo_membresia.id > 0:
            usuarios_basic.append(user.id)
    return usuarios_basic


def es_usuario_x_ancestro_de_usuario_y(ancestral_user, user):
    ancestral = User.objects.get(username=ancestral_user)
    while user.perfilusuario.padre:
        if user.perfilusuario.padre_id == ancestral.id:
            return True
        else:
            user = user.perfilusuario.padre.usuario
    return False


def obtener_total_ventas_de_articulo_de_miembro(miembro_id, last_month=True):
    """
    Recibe el id del miembro y devuelve la suma total de cada una de las ventas de ese miembro
    """
    miembro = User.objects.get(id=miembro_id)
    total = 0.0
    ventas = VentaArticulo.objects.filter(en_red_de_usuario=miembro, confirmada=True)
    # buscar solo las ventas ocurridas a partir de la ultima verificacion
    if last_month:
        last_verification = UserXDeliveredProfit.objects.last()
        if last_verification:
            ventas = ventas.filter(fecha_confirmacion__gte=last_verification.date)
    for venta in ventas:
        total += venta.precio
    return total


def obtener_total_ventas_de_paquetes_de_miembro(miembro_id, last_month=True):
    """
    Recibe el id del miembro y devuelve la suma total de cada una de las ventas de paquetes de bid de ese miembro
    """
    miembro = User.objects.get(id=miembro_id)
    total = 0.0
    ventas_paquetes = VentaPaqueteBid.objects.filter(en_red_de_usuario=miembro, confirmada=True)
    # buscar solo las ventas ocurridas a partir de la ultima verificacion
    if last_month:
        last_verification = UserXDeliveredProfit.objects.last()
        if last_verification:
            ventas_paquetes = ventas_paquetes.filter(fecha_confirmacion__gte=last_verification.date)
    for venta in ventas_paquetes:
        total += venta.precio
    return total


def obtener_plantilla_de_reto(reto):
    tipo_reto = reto.tipo_reto
    if tipo_reto.id == 1:
        return "Si consigues registrar a un total de %s personas con membresias %s antes de %s ganaras %s $" % \
               (reto.personas, reto.membresia, reto.tiempo, reto.dinero)
    if tipo_reto.id == 2:
        return "Si consigues hacer que %s usuarios de tu primera generacion pasen a una membresia %s antes de %s ganaras %s $." % \
               (reto.personas, reto.membresia, reto.tiempo, reto.dinero)
    if tipo_reto.id == 3:
        return "Si consigues vender %s dinero en paquetes de pujas, ganaras %s $." % (reto.dinero_pujas, reto.dinero)


def obtener_objeto_json(objeto):
    objeto_json = serializers.serialize('json', [objeto])
    return json.loads(objeto_json)[0]


def encriptar_usuario(nombre_usuario_plano):
    nombre_usuario_encriptado = encrypt(CLAVE, nombre_usuario_plano)
    # nombre_usuario_encriptado = nombre_usuario_plano
    return nombre_usuario_encriptado


def desencriptar_nombre_de_usuario(nombre_usuario_hexlified):
    usuario_texto_plano = decrypt(CLAVE, unhexlify(nombre_usuario_hexlified))
    return usuario_texto_plano


def obtener_usuario_desde_nombre_hexadecimal(nombre_usuario_hexlified):
    nombre_usuario = desencriptar_nombre_de_usuario(nombre_usuario_hexlified)
    return User.objects.get(username=nombre_usuario)


def obtener_usuario_random():
    users = User.objects.all()
    return random.choice(users)


def obtener_x_porciento_de(monto, porciento):
    return float(monto) * float(porciento) / 100


def obtener_comision_para_usuario(usuario):
    id_tipo_usuario = usuario.perfilusuario.tipo_usuario.id
    comision = 0
    if id_tipo_usuario == 1:
        comision = 5
    if id_tipo_usuario == 2:
        comision = 7
    if id_tipo_usuario == 3:
        comision = 8
    if id_tipo_usuario == 4:
        comision = 10
    if id_tipo_usuario == 5:
        comision = 10
    if id_tipo_usuario == 6:
        comision = 10
    if id_tipo_usuario == 7:
        comision = 10
    if id_tipo_usuario == 8:
        comision = 12

    return comision


def determinar_si_usuario_puede_cobrar_plan(usuario, plan):
    num_plan = plan.num_plan
    if num_plan == 1:
        return True
    if num_plan == 2:
        cant_user_en_red = usuario.perfilusuario.hijos.count()
        return usuario.perfilusuario.membresia_id > 1 and cant_user_en_red > 1 and usuario.perfilusuario.cantidad_de_puntos >= 50
    if num_plan == 3:
        return True
    if num_plan == 4:
        return usuario.perfilusuario.membresia_id > 1
    if num_plan == 5:
        return True
    if num_plan == 6:
        return usuario.perfilusuario.membresia_id > 1
    if num_plan == 7:
        return usuario.perfilusuario.membresia_id >= 8
    if num_plan == 8:
        cuenta_user = obtener_factura_total_de_usuario(usuario)
        return cuenta_user >= 100000
    if num_plan == 9:
        cuenta_user = obtener_factura_total_de_usuario(usuario)
        return cuenta_user >= 20000
    if num_plan == 10:
        cuenta_user = obtener_factura_total_de_usuario(usuario)
        return cuenta_user >= 15000
    if num_plan == 11:
        return True
    if num_plan == 12 or num_plan == 13 or num_plan == 14:
        return usuario.perfilusuario.tipo_usuario_id >= 4


def construir_mapa_de_estado_en_plan(usuario, plan, estado_mapa):
    # creamos un estado por cada requisito; sera una lista de 3 posiciones:
    # la primera posicion sera, -1 si esta por debajo, 0 si no se mide, 1 si esta por encima o lo cumple
    # para tipo_usuario *************************************
    tipo_usuario_lista = [0, '', '']
    if plan.tipo_usuario_id == 1:
        tipo_usuario_lista[0] = 0
    elif usuario.perfilusuario.tipo_usuario_id >= plan.tipo_usuario_id:
        tipo_usuario_lista[0] = 1
    else:
        tipo_usuario_lista[0] = -1
    tipo_usuario_lista[1] = usuario.perfilusuario.tipo_usuario.nombre
    tipo_usuario_lista[2] = plan.tipo_usuario.nombre
    estado_mapa['tipo_usuario'] = tipo_usuario_lista
    # para Tipo membresia ************************************
    tipo_membresia_lista = [0, '', '']
    if plan.membresia_minima_id == 1:
        tipo_membresia_lista[0] = 0
    elif usuario.perfilusuario.membresia_id >= plan.membresia_minima_id:
        tipo_membresia_lista[0] = 1
    else:
        tipo_membresia_lista[0] = -1
    tipo_membresia_lista[1] = usuario.perfilusuario.membresia.tipo_membresia.nombre
    tipo_membresia_lista[2] = plan.membresia_minima.nombre
    estado_mapa['tipo_membresia'] = tipo_membresia_lista
    # lista de usuarios en red ********************************
    usuarios_en_red_lista = [0, 0, 0]
    if plan.cantidad_de_usuarios_en_red == 0:
        usuarios_en_red_lista[0] = 0
    elif usuario.perfilusuario.hijos.count() > 1:
        usuarios_en_red_lista[0] = 1
    else:
        usuarios_en_red_lista[0] = -1
    usuarios_en_red_lista[1] = usuario.perfilusuario.hijos.count()
    usuarios_en_red_lista[2] = plan.cantidad_de_usuarios_en_red
    estado_mapa['usuarios_en_red'] = usuarios_en_red_lista
    # cantidad de puntos lista ***********************************
    cantidad_ptos_lista = [0, 0, 0]
    if plan.cantidad_de_puntos == 0:
        cantidad_ptos_lista[0] = 0
    elif usuario.perfilusuario.cantidad_de_puntos >= plan.cantidad_de_puntos:
        cantidad_ptos_lista[0] = 1
    else:
        cantidad_ptos_lista[0] = -1
    cantidad_ptos_lista[1] = usuario.perfilusuario.cantidad_de_puntos
    cantidad_ptos_lista[2] = plan.cantidad_de_puntos
    estado_mapa['cantidad_de_puntos'] = cantidad_ptos_lista
    # cantidad de dinero lista ***************************************
    factura_total = obtener_factura_total_de_usuario(usuario)
    cantidad_de_dinero_lista = [0, 0, 0]
    if plan.cantidad_de_dinero == 0:
        cantidad_de_dinero_lista[0] = 0
    elif factura_total >= plan.cantidad_de_dinero:
        cantidad_de_dinero_lista[0] = 1
    else:
        cantidad_de_dinero_lista[0] = -1
    cantidad_de_dinero_lista[1] = factura_total
    cantidad_de_dinero_lista[2] = plan.cantidad_de_dinero
    estado_mapa['cantidad_de_dinero'] = cantidad_de_dinero_lista

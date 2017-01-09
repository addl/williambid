import datetime
from datetime import time
from itertools import chain
import random
from back_office.models import PerfilUsuario, Membresia, TipoUsuario
from back_office.util import obtener_usuario_random
from williambid.utils import generar_simple_nick

__author__ = 'bryan'

from williambid.models import *

# esto metodo solo es llamado por Robots o usuarios conectados, a traves de la view pujar
# el usuario es el usuario de django que esta en base datos
def pujar_subasta(id_subasta, usuario):
    subasta = Subasta.objects.get(id=id_subasta)
    if subasta is not None and not subasta_terminada(subasta):
        subasta.precio_actual = subasta.precio_actual + 0.01
        tiempo_expiracion = timedelta(hours=subasta.tiempo_regresivo.hour, minutes=subasta.tiempo_regresivo.minute,
                                      seconds=subasta.tiempo_regresivo.second)
        subasta.fecha_expiracion = datetime.now() + tiempo_expiracion
        subasta.ganador = usuario
        print "Pujando la subasta %s, expirara en %s aproximadamente" % (subasta, subasta.fecha_expiracion)
        subasta.save(update_fields=['precio_actual', 'fecha_expiracion', 'ganador'])
        return subasta
    return None


def subasta_terminada(subasta):
    if subasta.fecha_expiracion > datetime.now():
        return False
    return True


def buscar_subastas(querysearch, language):
    if language == 'en-us':
        return Subasta.objects.filter(contenido__nombre_en_us__icontains=querysearch, estado=Subasta.ACTIVE)
    return Subasta.objects.filter(articulo__nombre_es_es__icontains=querysearch, terminada=False)


def obtener_subastas_pujando():
    fechaActual = datetime.now()
    # segundos para garantizar que sean vistas con tiempo
    fechaMasUnosSegundos = fechaActual + timedelta(seconds=2)
    # Para las subastas que estan en marcha
    subastas_en_marcha = Subasta.objects.filter(estado=Subasta.ACTIVE, fecha_expiracion__gte=fechaMasUnosSegundos)
    return subastas_en_marcha


def obtener_subastas_vendidas_recientemente():
    # devolvemos solo las 2 ultimas
    return list(obtener_subastas_vendidas())[-2:]


def obtener_subastas_vendidas():
    # esto es por si el server estuvo caido, es bueno verificar todas las vencidas y setearlas como terminada
    desactivar_subastas_vendidas()
    # subastas q ya se vendieron recientemente, las mas recientes delante
    subastas_terminadas = Subasta.objects.filter(estado=Subasta.FINISHED).order_by('fecha_expiracion')
    return subastas_terminadas


def desactivar_subastas_vendidas():
    # esto es por si el server estuvo caido, es bueno verificar todas las vencidas y setearlas como terminada
    subastas_expiradas = Subasta.objects.filter(fecha_expiracion__lte=datetime.now())
    for p in subastas_expiradas:
        p.estado = Subasta.FINISHED
        p.save(force_update=True)


def crear_subasta_de_valores_x_defecto(articulo):
    p = Subasta()
    p.contenido = articulo
    p.tipo_subasta = TipoSubasta.objects.first()
    #p.activa = True
    now = datetime.now() + timedelta(hours=12)
    p.fecha_inicio = now
    p.tiempo_regresivo = time(0, 1)
    p.fecha_expiracion = p.fecha_inicio + timedelta(minutes=p.tiempo_regresivo.minute)
    precio_minimo = articulo.precio
    # el precio a partir del cual comienza a pujarse
    # por el momento se calculara el 15 % menor al precio minimo
    p.precio_actual = precio_minimo - (precio_minimo * 15 / 100)
    p.gana_robot = True
    # p.estado = 1   # this is by default
    p.ganador = None
    return p


def crear_subasta_vendida_a_partir_de_subasta(subasta):
    print "Saving subasta vendida with subasta %s and shopingcart %s" % (subasta, subasta.ganador.shoppinggcart)
    p = SubastaVendida(subasta=subasta, shoping_cart=subasta.ganador.shoppinggcart)
    # p.contenido = subasta.contenido
    # p.tipo_subasta = subasta.tipo_subasta
    # p.fecha_inicio = subasta.fecha_inicio
    # p.tiempo_regresivo = subasta.tiempo_regresivo
    # p.fecha_expiracion =subasta.fecha_expiracion
    # p.precio_actual = subasta.precio_actual
    # p.gana_robot = subasta.gana_robot
    # p.estado = subasta.estado
    # p.ganador = subasta.ganador
    return p


def crear_subasta_de_paquete_de_bid(paquete_bid):
    p = Subasta()
    p.contenido = paquete_bid
    p.tipo_subasta = TipoSubasta.objects.first()
    #p.activa = True
    now = datetime.now() + timedelta(hours=12)
    p.fecha_inicio = now
    p.tiempo_regresivo = time(0, 1)
    p.fecha_expiracion = p.fecha_inicio + timedelta(minutes=p.tiempo_regresivo.minute)
    precio_minimo = paquete_bid.precio
    # el precio a partir del cual comienza a pujarse
    # por el momento se calculara el 10 % menor al precio minimo
    p.precio_actual = precio_minimo - (precio_minimo * 10 / 100)
    p.gana_robot = True
    p.estado = Subasta.ACTIVE
    p.ganador = None
    return p


def crear_usuario_para_robot():
    usuario = User()
    try:
        # nick entre 5 y 8 caracteres
        seudonimo = generar_simple_nick(random.randint(5, 8))
        # creamos el usuario q representa al robot
        usuario.username = seudonimo
        usuario.save()
        # creamos y asignamos el perfil que tiene ciudad, direccion, etc
        perfil_usuario = PerfilUsuario()
        perfil_usuario.seudonimo = seudonimo
        perfil_usuario.usuario = usuario
        # asignamos el tipo de usuario
        tipo_usuario = random.choice(TipoUsuario.objects.all())
        perfil_usuario.tipo_usuario = tipo_usuario
        # asignamos membrasia a los usuarios robot aleatoriamente
        membresia = random.choice(Membresia.objects.all())
        print "Asignando a robot %s la membresia %s" % (seudonimo, membresia.tipo_membresia.nombre)
        perfil_usuario.membresia = membresia
        # asignamos un padre al usuario
        parent = random.choice(User.objects.exclude(id=usuario.id))
        print "Asignando a robot %s su papa, %s" % (seudonimo, parent)
        perfil_usuario.padre = parent.perfilusuario
        perfil_usuario.save()
        # creamos el robot en la base de datos
        robot_db = Robot()
        robot_db.usuario = usuario
        robot_db.save()
        print "Creado robot %s" % seudonimo
        # es posible que el seudonimo ya este en base de datos y como es unico
        # pq tambien se usa para username, puede haber excepcion
    except Exception, e:
        print(e)
        # return crear_usuarios_para_robots()
    return usuario


def verificar_que_articulo_no_este_en_puja(articulo_id):
    subastas = obtener_subastas_pujando()
    for p in subastas:
        if p.contenido.id == articulo_id:
            print "Articulo %s esta ya en subastas..." % articulo_id
            return True
    return False
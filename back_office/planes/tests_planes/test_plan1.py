import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "william.settings")
django.setup()


import random
from django.contrib.auth.models import User
from williambid.models import Articulo, VentaPaqueteBid, VentaArticulo, PaqueteBid
from back_office.planes.manager_planes import PlanesManagerSingleton

from williambid.service_layer import crear_usuario_para_robot


__author__ = 'bryan'

articulos = Articulo.objects.all()
usuarios = User.objects.all()
cant_art = len(articulos)
cant_users = len(usuarios)


def crear_articulos_de_prueba():
    if len(articulos) == 0:
        for i in range(4):
            art = Articulo(cantidad_de_articulos=20, precio=20.0, pujas_automaticas=True)
            art.save(force_insert=True)

def crear_usuario_robots_de_prueba():
    if len(usuarios) < 2:
        for i in range(5):
            crear_usuario_para_robot()


def crear_ventas(cant):
    for i in range(0, cant):
        usuario_red_owner = usuarios[random.randint(0, cant_users - 1)]
        a_usuario = usuarios[random.randint(0, cant_users - 1)]
        articulo = articulos[random.randint(0, cant_art - 1)]
        precio = random.randint(20, 40)
        venta = VentaArticulo(en_red_de_usuario=usuario_red_owner, articulo=articulo, precio=precio, a_usuario=a_usuario.id)
        venta.save(force_insert=True)
        num = random.randint(0, 100)
        if num % 4 == 0:
            pkt = PaqueteBid(nombre="Pakete100", descripcion="Descrpcion Pakete", cantidad_de_bids=100, precio=50)
            pkt.save(force_insert=True)
            print "Creando venta de paquete BID de precio %s para usuario %s" % (precio, usuario_red_owner)
            ventapaquete = VentaPaqueteBid(en_red_de_usuario=usuario_red_owner, precio=precio, paquete=pkt, a_usuario=a_usuario.id)
            ventapaquete.save(force_insert=True)
        else:
            print "Creando venta de precio %s para usuario %s" % (precio, usuario_red_owner)

def crear_ventas_pkt_bids(cant):
    for i in range(0, cant):
        usuario_red_owner = usuarios[random.randint(0, cant_users - 1)]
        a_usuario = usuarios[random.randint(0, cant_users - 1)]
        precio = random.randint(20, 40)
        pkt = PaqueteBid(nombre="Pakete100", descripcion="Descrpcion Pakete", cantidad_de_bids=100, precio=50)
        pkt.save(force_insert=True)
        print "Creando venta de paquete BID de precio %s para usuario %s" % (precio, usuario_red_owner)
        ventapaquete = VentaPaqueteBid(en_red_de_usuario=usuario_red_owner, precio=precio, paquete=pkt, a_usuario=a_usuario.id)
        ventapaquete.save(force_insert=True)


if __name__ == '__main__':
    #crear_usuario_robots_de_prueba()
    #crear_articulos_de_prueba()
    #crear_ventas(12)
    #crear_ventas_pkt_bids(10)
    plan_manager = PlanesManagerSingleton.get_instance()
    plan_manager.plan_compensacion_uno.asignar_ganancia_a_cada_usuario()
    print "END EXECUTION"
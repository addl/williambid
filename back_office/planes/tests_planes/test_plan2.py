import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "william.settings")
django.setup()


import random
from django.contrib.auth.models import User
from williambid.models import Articulo, VentaPaqueteBid, VentaArticulo, PaqueteBid
from back_office.planes.manager_planes import PlanesManagerSingleton

__author__ = 'bryan'

articulos = Articulo.objects.all()
usuarios = User.objects.all()
cant_art = len(articulos)
cant_users = len(usuarios)


def crear_ventas(cant):
    for i in range(0, cant):
        usuario = usuarios[random.randint(0, cant_users - 1)]
        articulo = articulos[random.randint(0, cant_art - 1)]
        precio = random.randint(20, 40)
        venta = VentaArticulo(en_red_de_usuario=usuario, articulo=articulo, precio=precio)
        venta.save(force_insert=True)
        num = random.randint(0, 100)
        if num % 4 == 0:
            pkt = PaqueteBid(nombre="Pakete100", descripcion="Descrpcion Pakete", cantidad=100, precio=50)
            pkt.save(force_insert=True)
            print "Creando venta de paquete BID de precio %s para usuario %s" % (precio, usuario)
            ventapaquete = VentaPaqueteBid(en_red_de_usuario=usuario, articulo=articulo, precio=precio, paquete=pkt)
            ventapaquete.save(force_insert=True)
        else:
            print "Creando venta de precio %s para usuario %s" % (precio, usuario)

from williambid.service_layer import crear_usuario_para_robot

if __name__ == '__main__':
    plan_manager = PlanesManagerSingleton.get_instance()
    res = plan_manager.plan_compensacion_dos.asignar_ganancias_a_usuarios()
    print res
import datetime
from datetime import timedelta
from django.contrib.auth.models import User
from back_office.models import Membresia
from back_office.planes.compensacion5 import PlanCompensacionCinco
import logging

from back_office.planes.utils import obtener_lista_de_usuarios

log = logging.getLogger(__name__)
__author__ = 'bryan'


class PlanCompensacionOnce():

    def __init__(self):
        log.info("Creating %s" % self.__class__)
        self.NUMERO_PLAN = 11

    def analizar_membresias_de_todos_los_usuarios(self):
        log.info("PLan %s AUTOENRIQUECIMIENTO. Anilizando membresia de cada usuario" % self.NUMERO_PLAN)
        fecha_actual = datetime.datetime.now()
        # analizamos a todos los usuarios execpto admin(EMPRESA) y robots(depende de la configuracion en settings)
        usuarios = obtener_lista_de_usuarios()
        for u in usuarios:
            monto_usuario = 0
            lista_cuentas = u.bancousuario_set.all()
            for cuenta in lista_cuentas:
                transacciones = cuenta.historialtransacciones_set.all()
                for tran in transacciones:
                    monto_usuario += tran.deposito

            tipo_membresia = self.__membresia_minima(monto_usuario)
            if tipo_membresia > u.perfilusuario.membresia.tipo_membresia.id:
                u.perfilusuario.membresia = Membresia.objects.get(tipo_membresia=tipo_membresia)
                u.perfilusuario.fecha_obtuvo_membresia = fecha_actual
                u.perfilusuario.save(force_update=True)
                log.info("Asignando membresia: %s a usuario: %s " % (u.perfilusuario.membresia, u))
                # **********************************IMPORTANTE ****************************
                # avisar al plan 5 del camio de membresia
                PlanCompensacionCinco.computar_cambio_de_membresia(u)
            elif tipo_membresia < u.perfilusuario.membresia.tipo_membresia.id:
                fecha_obtuvo_membresia = u.perfilusuario.fecha_obtuvo_membresia
                fecha_obtuvo_membresia_mas_1_mes = fecha_obtuvo_membresia + timedelta(days=30)
                # si se cumplio un mes de tenerla, se la quitamos
                if fecha_obtuvo_membresia_mas_1_mes >= fecha_actual:
                    u.perfilusuario.membresia = Membresia.objects.get(tipo_membresia=tipo_membresia)
                    u.perfilusuario.fecha_obtuvo_membresia = fecha_actual
                    u.perfilusuario.save(force_update=True)


    def __membresia_minima(self, monto_usuario):
        if monto_usuario >= 5000:
            return 9
        if monto_usuario >= 3000:
            return 8
        if monto_usuario >= 2000:
            return 7
        if monto_usuario >= 1000:
            return 6
        if monto_usuario >= 500:
            return 5
        if monto_usuario >= 250:
            return 4
        if monto_usuario >= 100:
            return 3
        if monto_usuario >= 10:
            return 2

        return 1
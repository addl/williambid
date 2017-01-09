import datetime
from datetime import timedelta
from django.contrib.auth.models import User
from back_office.banco import obtener_factura_total_de_usuario, depositar_monto_en_cuenta_de_usuario
from back_office.models import BancoUsuario
import logging

log = logging.getLogger(__name__)
__author__ = 'bryan'


class PlanCompensacionDiez():

    def __init__(self):
        log.info("Creating %s" % self.__class__)
        self.NUMERO_PLAN = 10

    # si logran facturar 15000 USD en los 1ros 31 dias despues de hacerse miembros
    def evaluar_usuarios(self):
        log.info("Plan %s: BONO 31 DIAS verificando..." % self.NUMERO_PLAN)
        now = datetime.datetime.now()
        ahora_menos_31_dias = now - timedelta(days=31)
        # usuario que se unieron hace menos de igual a 31 dias
        usuarios_en_rango_de_plan = User.objects.filter(date_joined__gte=ahora_menos_31_dias)
        for user in usuarios_en_rango_de_plan:
            monto_usuario = obtener_factura_total_de_usuario(user, except_plan=self.NUMERO_PLAN)
            if monto_usuario >= 15000:
                monto_cuenta_de_este_plan = obtener_factura_total_de_usuario(user, only_plan=self.NUMERO_PLAN)
                # si no hay dinero en esta cuenta, entonces depositamos, de lo contrario
                if monto_cuenta_de_este_plan == 0:
                    depositar_monto_en_cuenta_de_usuario(user.id, 1000, self.NUMERO_PLAN)
        log.info("Plan %s evaluacion de usuario exitosamente" % self.NUMERO_PLAN)

from back_office.models import BancoUsuario
import logging

log = logging.getLogger(__name__)
__author__ = 'bryan'

from back_office.banco import depositar_monto_en_cuenta_de_usuario
from django.contrib.auth.models import User


class PlanCompensacionOcho():
    NUMERO_PLAN = 8

    def __init__(self):
        log.info("Creating %s" % self.__class__)
        user_admin = User.objects.get(is_superuser=1)
        if not user_admin:
            log.error("No puedo crear el Plan No. 8. Usuario admin no encontrado")
            raise "No puedo crear el Plan No. 8. Usuario admin no encontrado"

    def asignar_beneficio_facturacion_global(self, beneficios):
        log.info("Plan %s: BENEFICIOS DE EMPRESA VIP y VIP PRO. Asignando beneficios." % self.NUMERO_PLAN)
        users = User.objects.all()
        por_ciento = beneficios * 3 / 100

        for user in users:
            total_cuenta = 0
            banco_cuentas = BancoUsuario.objects.filter(usuario=user)
            for banco_cuenta in banco_cuentas:
                total_cuenta = banco_cuenta.monto_total + total_cuenta
            # print 'total de la cuenta de facturacion %s a user %s '% (total_cuenta, user.username)
            if total_cuenta > 100000:
                depositar_monto_en_cuenta_de_usuario(user.id, por_ciento, self.NUMERO_PLAN)
        log.info("Plan %s: Beneficios asignados exitosamente" % self.NUMERO_PLAN)

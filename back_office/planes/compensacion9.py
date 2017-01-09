from django.contrib.auth.models import User
from back_office.banco import obtener_factura_total_de_usuario, depositar_monto_en_cuenta_de_usuario
import logging

from back_office.planes.utils import obtener_lista_de_usuarios

log = logging.getLogger(__name__)
__author__ = 'bryan'


class PlanCompensacionNueve():

    def __init__(self):
        log.info("Creating %s" % self.__class__)
        self.NUMERO_PLAN = 9
        user_admin = User.objects.get(is_superuser=1)
        if not user_admin:
            log.error("No puedo crear el Plan No. 9. Usuario admin no encontrado")
            raise "No puedo crear el Plan No. 9. Usuario admin no encontrado"

    def asignar_beneficios_usuarios(self):
        log.info("Plan %s: BENEFICIOS DE EMPRESA FONDO GLOBAL DE LIDRAZGO. Asignando beneficios." % self.NUMERO_PLAN)
        users = obtener_lista_de_usuarios(exclude_admin=False)
        for user in users:
            total_cuenta = obtener_factura_total_de_usuario(user, except_plan=9)
            # en la division hay que garantizar quedarnos con un entero
            cantidad = 1000 * (int(total_cuenta / 20000))
            if cantidad > 0:
                depositar_monto_en_cuenta_de_usuario(user.id, cantidad, self.NUMERO_PLAN)
        log.info("Plan %s: Beneficios asignados exitosamente" % self.NUMERO_PLAN)
from back_office.banco import depositar_monto_en_cuenta_de_usuario
from django.contrib.auth.models import User
import logging

log = logging.getLogger(__name__)
__author__ = 'bryan'


class PlanCompensacionSiete():
    NUMERO_PLAN = 7

    def __init__(self):
        log.info("Creating %s" % self.__class__)
        user_admin = User.objects.get(is_superuser=1)
        if not user_admin:
            log.error("No puedo crear el Plan No. 7. Usuario admin no encontrado")
            raise "No puedo crear el Plan No. 7. Usuario admin no encontrado"


    def asignar_beneficio_total_empresa_socios_VIP_PRO(self, beneficios):
        log.info("Plan %s: Asignando beneficios..." % self.NUMERO_PLAN)
        users = User.objects.all()
        por_ciento = beneficios * 2 / 100
        for user in users:
            if user.perfilusuario.membresia.tipo_membresia.id == 8 or user.perfilusuario.membresia.tipo_membresia.id == 9:
                depositar_monto_en_cuenta_de_usuario(user.id, por_ciento, self.NUMERO_PLAN)
        log.info("Plan %s: Beneficios asignados exitosamente" % self.NUMERO_PLAN)


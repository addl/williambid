from django.contrib.auth.models import User
from back_office.banco import depositar_monto_en_cuenta_de_usuario
import logging
log = logging.getLogger(__name__)

__author__ = 'bryan'




class PlanCompensacionDos():
    """Arbol binario hibrido"""
    def __init__(self, arbol_binario_hibrido):
        log.info("Creating %s" % self.__class__)
        self.NUMERO_PLAN = 2
        self.arbol_binario_hibrido = arbol_binario_hibrido

    def asignar_ganancias_a_usuarios(self):
        """
        IMPORTANTE: PARA COBRAR EN EL BINARIO TIENES QUE CUMPLIR 3 REGLAS:
            1.	TENER UNA MEMBRESIA DE PAGO.
            2.	TENER MiNIMO DOS USUARIOS DIRECTOS EN TU RED.
            3.	TENER MiNIMO 50 PUNTOS
        """
        log.info("Plan %s: BINARIO HIBRIDO....Asignando ganancias" % self.NUMERO_PLAN)
        resultados = {}
        self.arbol_binario_hibrido.evaluar_arbol(resultados)
        for user_id, factura in resultados.items():
            user = User.objects.get(id=user_id)
            ptos = user.perfilusuario.cantidad_de_puntos
            tipo_mem = user.perfilusuario.membresia.tipo_membresia.id
            if factura > 0 and ptos >= 50 and tipo_mem > 1:
                # en el doc del binario se establece un limite de cobro mensual de 10000
                cantidad_a_transferir = factura
                if factura > 100000:
                    cantidad_a_transferir = 100000
                depositar_monto_en_cuenta_de_usuario(user_id, cantidad_a_transferir, self.NUMERO_PLAN)
        log.info("Plan %s: retornando resultados de evaluacion" % self.NUMERO_PLAN)
        return resultados

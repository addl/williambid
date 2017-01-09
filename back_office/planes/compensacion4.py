from back_office.banco import depositar_monto_en_cuenta_de_usuario
import logging
log = logging.getLogger(__name__)

__author__ = 'bryan'




class PlanCompensacionCuatro():

    def __init__(self, arbol_binario):
        log.info("Creating %s" % self.__class__)
        self.arbol_binario = arbol_binario
        self.NUMERO_PLAN = 4

    def asignar_ganancia_a_usuarios(self):
        log.info("Plan %s: BINARIO POR DERRAME DE EMPRESA MENSUAL. Asignando ganancias." % self.NUMERO_PLAN)
        map_user_monto = {}
        # este mapa usado como referencia, devuelve el clave:valor que corresponnde con usuario:monto total
        self.arbol_binario.evaluar_arbol(map_user_monto)
        for user_id, monto in map_user_monto.items():
            # este metodo se encarga de devolver la ganancia obteneida por el plan
            depositar_monto_en_cuenta_de_usuario(user_id, monto, self.NUMERO_PLAN)
        log.info("Plan %s asignacion de ganancia terminada " % self.NUMERO_PLAN)
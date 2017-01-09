from back_office.banco import depositar_monto_en_cuenta_de_usuario
import logging

log = logging.getLogger(__name__)

__author__ = 'bryan'

class PlanCompensacionUno():

    def __init__(self, arbol_general):
        log.info("Creating %s" % self.__class__)
        self.NUMERO_PLAN = 1
        self.arbol_general = arbol_general

    def asignar_ganancia_a_cada_usuario(self):
        log.info("Plan %s: RED INFINITA 2,4,6,10,15,20...Asignando ganancias" % self.NUMERO_PLAN)
        mapa = {}
        self.arbol_general.obtener_ganancia_por_nodo(mapa)
        for miembro_id, ganancia in mapa.items():
            depositar_monto_en_cuenta_de_usuario(miembro_id, ganancia, self.NUMERO_PLAN)
        log.info("Plan %s: Asignacion de ganancias finalizado" % self.NUMERO_PLAN)



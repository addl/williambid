from django.contrib.auth.models import User
from back_office.banco import depositar_monto_en_cuenta_de_usuario, obtener_factura_total_de_usuario
from back_office.util import obtener_x_porciento_de, obtener_total_ventas_de_articulo_de_miembro, \
    obtener_total_ventas_de_paquetes_de_miembro
import logging
log = logging.getLogger(__name__)

__author__ = 'bryan'




class PlanCompensacionTres():


    def __init__(self, arbol_gral):
        self.NUMERO_PLAN = 3
        self.arbol_gral = arbol_gral


    def evaluar_usuarios(self):
        """
            Recorrer el arbol y evaluar nodo x nodo
        """
        log.info("Plan %s: PLAN UNILEVEL DE VENTA DIRECTA DE PUJAS: Asignando ganancias." % self.NUMERO_PLAN)
        cola = []
        cola.append(self.arbol_gral)
        while len(cola) > 0:
            frente = cola.__getitem__(0)
            cola.remove(frente)
            self.__evaluar_un_usuario(frente)
            for sub_arbol in frente.lista_subarboles:
                cola.append(sub_arbol)
        log.info("Plan %s evaluacion terminada con exito " % self.NUMERO_PLAN)


    def __evaluar_un_usuario(self, arbol_usuario):
        usuario = arbol_usuario.raiz
        tipo_membresia_id = usuario.perfilusuario.membresia.id
        # segun la tabla, el comportamiento para los niveles 2 a 7 es el mismo, independinte del tipo de usuario
        # solo varia el % del nivel 1
        x_ciento_nivel_2 = obtener_x_porciento_de(self.__evaluar_nivel_de_red_para(arbol_usuario, 2), 5)
        x_ciento_nivel_3 = obtener_x_porciento_de(self.__evaluar_nivel_de_red_para(arbol_usuario, 3), 5)
        x_ciento_nivel_4 = obtener_x_porciento_de(self.__evaluar_nivel_de_red_para(arbol_usuario, 4), 5)
        x_ciento_nivel_5 = obtener_x_porciento_de(self.__evaluar_nivel_de_red_para(arbol_usuario, 5), 5)
        x_ciento_nivel_6 = obtener_x_porciento_de(self.__evaluar_nivel_de_red_para(arbol_usuario, 6), 5)
        x_ciento_nivel_7 = obtener_x_porciento_de(self.__evaluar_nivel_de_red_para(arbol_usuario, 7), 10)
        if tipo_membresia_id == 1:
            x_ciento_nivel_1 = obtener_x_porciento_de(self.__evaluar_nivel_de_red_para(arbol_usuario, 1), 10)
            total = x_ciento_nivel_1 + x_ciento_nivel_2 + x_ciento_nivel_3 + x_ciento_nivel_4 + x_ciento_nivel_5 + x_ciento_nivel_6 + x_ciento_nivel_7
            depositar_monto_en_cuenta_de_usuario(usuario.id, total, self.NUMERO_PLAN)
        if tipo_membresia_id == 2:
            x_ciento_nivel_1 = obtener_x_porciento_de(self.__evaluar_nivel_de_red_para(arbol_usuario, 1), 25)
            total = x_ciento_nivel_1 + x_ciento_nivel_2 + x_ciento_nivel_3 + x_ciento_nivel_4 + x_ciento_nivel_5 + x_ciento_nivel_6 + x_ciento_nivel_7
            depositar_monto_en_cuenta_de_usuario(usuario.id, total, self.NUMERO_PLAN)
        if tipo_membresia_id == 3:
            x_ciento_nivel_1 = obtener_x_porciento_de(self.__evaluar_nivel_de_red_para(arbol_usuario, 1), 30)
            total = x_ciento_nivel_1 + x_ciento_nivel_2 + x_ciento_nivel_3 + x_ciento_nivel_4 + x_ciento_nivel_5 + x_ciento_nivel_6 + x_ciento_nivel_7
            depositar_monto_en_cuenta_de_usuario(usuario.id, total, self.NUMERO_PLAN)
        if tipo_membresia_id == 4:
            x_ciento_nivel_1 = obtener_x_porciento_de(self.__evaluar_nivel_de_red_para(arbol_usuario, 1), 35)
            total = x_ciento_nivel_1 + x_ciento_nivel_2 + x_ciento_nivel_3 + x_ciento_nivel_4 + x_ciento_nivel_5 + x_ciento_nivel_6 + x_ciento_nivel_7
            depositar_monto_en_cuenta_de_usuario(usuario.id, total, self.NUMERO_PLAN)
        if tipo_membresia_id == 5:
            x_ciento_nivel_1 = obtener_x_porciento_de(self.__evaluar_nivel_de_red_para(arbol_usuario, 1), 40)
            total = x_ciento_nivel_1 + x_ciento_nivel_2 + x_ciento_nivel_3 + x_ciento_nivel_4 + x_ciento_nivel_5 + x_ciento_nivel_6 + x_ciento_nivel_7
            depositar_monto_en_cuenta_de_usuario(usuario.id, total, self.NUMERO_PLAN)
        if tipo_membresia_id == 6:
            x_ciento_nivel_1 = obtener_x_porciento_de(self.__evaluar_nivel_de_red_para(arbol_usuario, 1), 45)
            total = x_ciento_nivel_1 + x_ciento_nivel_2 + x_ciento_nivel_3 + x_ciento_nivel_4 + x_ciento_nivel_5 + x_ciento_nivel_6 + x_ciento_nivel_7
            depositar_monto_en_cuenta_de_usuario(usuario.id, total, self.NUMERO_PLAN)
        # membresia de la 7 a la 9 es el mismo porcentaje
        if tipo_membresia_id == 7 or tipo_membresia_id == 8 or tipo_membresia_id == 9:
            x_ciento_nivel_1 = obtener_x_porciento_de(self.__evaluar_nivel_de_red_para(arbol_usuario, 1), 50)
            total = x_ciento_nivel_1 + x_ciento_nivel_2 + x_ciento_nivel_3 + x_ciento_nivel_4 + x_ciento_nivel_5 + x_ciento_nivel_6 + x_ciento_nivel_7
            depositar_monto_en_cuenta_de_usuario(usuario.id, total, self.NUMERO_PLAN)


    def __evaluar_nivel_de_red_para(self, arbol_usuario, nivel):
        print("WARMING: Evaluando ventas en red instead Ventas de Pujas Directas en plan %s" % self.NUMERO_PLAN)
        if nivel < 0:
            raise "NO puedo evaluar nivel de arbol menor que cero"
        if nivel == 0:
            # buscar solamente las ventas de paquetes de pujas en la red del usuario
            total_ventas_paquetes_de_pujas_directas = obtener_total_ventas_de_paquetes_de_miembro(arbol_usuario.raiz.id)
            return total_ventas_paquetes_de_pujas_directas
        suma = 0.0
        nivel -= 1
        for sub_arbol in arbol_usuario.lista_subarboles:
            suma += self.__evaluar_nivel_de_red_para(sub_arbol, nivel)
        return suma
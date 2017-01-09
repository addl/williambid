from back_office.banco import obtener_factura_total_de_usuario, depositar_monto_en_cuenta_de_usuario
from back_office.util import obtener_x_porciento_de
import logging

log = logging.getLogger(__name__)
__author__ = 'bryan'


class PlanCompensacion_12_13_14():
    """
    """
    def __init__(self, arbol_gral):
        log.info("Creating %s" % self.__class__)
        self.NUMERO_PLAN = 121314
        self.arbol_general = arbol_gral


    def evaluar_usuarios(self):
        """
            Recorrer el arbol y evaluar nodo pr nodo
        """
        log.info("Plan %s: DE IGUALUACION. Iniciando recorrido para planes 12, 13 y 14" % self.NUMERO_PLAN)
        cola = []
        cola.append(self.arbol_general)
        while len(cola) > 0:
            frente = cola.__getitem__(0)
            cola.remove(frente)
            self.__evaluar_un_usuario_12(frente)
            self.__evaluar_un_usuario_13(frente)
            self.__evaluar_un_usuario_14(frente)
            for sub_arbol in frente.lista_subarboles:
                cola.append(sub_arbol)
        log.info("Evaluacion de planes 12, 13 y 14 culminada exitosamente")


    def __evaluar_un_usuario_12(self, arbol_usuario):
        plan_evaluando = 12
        usuario = arbol_usuario.raiz
        tipo_usuario_id = usuario.perfilusuario.tipo_usuario.id
        if tipo_usuario_id > 4:
            if tipo_usuario_id == 4:
                # solo el nivel uno, y el 2%
                suma_nivel = self.__evaluar_nivel_de_red_para_12(arbol_usuario, 1)
                depositar_monto_en_cuenta_de_usuario(usuario.id, obtener_x_porciento_de(suma_nivel, 2), plan_evaluando)
            if tipo_usuario_id == 5:
                # solo el nivel uno, y el 5%
                suma_nivel = self.__evaluar_nivel_de_red_para_12(arbol_usuario, 1)
                depositar_monto_en_cuenta_de_usuario(usuario.id, obtener_x_porciento_de(suma_nivel, 5), plan_evaluando)
            if tipo_usuario_id == 6:
                # primer y segundo nivel, 5 y 2 % respectivamente
                x_ciento_nivel_uno = obtener_x_porciento_de(self.__evaluar_nivel_de_red_para_12(arbol_usuario, 1), 5)
                x_ciento_nivel_dos = obtener_x_porciento_de(self.__evaluar_nivel_de_red_para_12(arbol_usuario, 2), 2)
                depositar_monto_en_cuenta_de_usuario(usuario.id, x_ciento_nivel_uno + x_ciento_nivel_dos, plan_evaluando)
            if tipo_usuario_id == 7:
                # nivel uno, dos y tres, con % 5,2,2 respectivamente
                x_ciento_nivel_uno = obtener_x_porciento_de(self.__evaluar_nivel_de_red_para_12(arbol_usuario, 1), 5)
                x_ciento_nivel_dos = obtener_x_porciento_de(self.__evaluar_nivel_de_red_para_12(arbol_usuario, 2), 2)
                x_ciento_nivel_tres = obtener_x_porciento_de(self.__evaluar_nivel_de_red_para_12(arbol_usuario, 3), 2)
                depositar_monto_en_cuenta_de_usuario(usuario.id,
                                                     x_ciento_nivel_uno + x_ciento_nivel_dos + x_ciento_nivel_tres, plan_evaluando)
            if tipo_usuario_id == 8:
                # nivel uno, dos, tres y cuatro, con % 5,2,2,5 respectivamente
                x_ciento_nivel_uno = obtener_x_porciento_de(self.__evaluar_nivel_de_red_para_12(arbol_usuario, 1), 5)
                x_ciento_nivel_dos = obtener_x_porciento_de(self.__evaluar_nivel_de_red_para_12(arbol_usuario, 2), 2)
                x_ciento_nivel_tres = obtener_x_porciento_de(self.__evaluar_nivel_de_red_para_12(arbol_usuario, 3), 2)
                x_ciento_nivel_cuatro = obtener_x_porciento_de(self.__evaluar_nivel_de_red_para_12(arbol_usuario, 4), 5)
                depositar_monto_en_cuenta_de_usuario(usuario.id,
                                                     x_ciento_nivel_uno + x_ciento_nivel_dos + x_ciento_nivel_tres +
                                                     x_ciento_nivel_cuatro, plan_evaluando)


    def __evaluar_nivel_de_red_para_12(self, arbol_usuario, nivel):
        if nivel < 0:
            raise "NO puedo evaluar nivel de arbol menor que cero"
        if nivel == 0:
            return obtener_factura_total_de_usuario(arbol_usuario.raiz)
        suma = 0
        nivel -= 1
        for sub_arbol in arbol_usuario.lista_subarboles:
            suma += self.__evaluar_nivel_de_red_para_12(sub_arbol, nivel)
        return suma



    """
    *****************************************************************************************************
    ***************************************PLAN DE COMPENSACION 13***************************************
    ***************************************PLAN DE COMPENSACION 13***************************************
    ***************************************PLAN DE COMPENSACION 13***************************************
    *****************************************************************************************************
    """
    def __evaluar_un_usuario_13(self, arbol_usuario):
        plan_evaluando = 13
        usuario = arbol_usuario.raiz
        tipo_usuario_id = usuario.perfilusuario.tipo_usuario.id
        if tipo_usuario_id > 4:
            if tipo_usuario_id == 4:
                # solo el nivel uno, y el 2%
                suma_nivel = self.__evaluar_nivel_de_red_para_13(arbol_usuario, 1)
                depositar_monto_en_cuenta_de_usuario(usuario.id, obtener_x_porciento_de(suma_nivel, 2), plan_evaluando)
            if tipo_usuario_id == 5:
                # solo el nivel uno, y el 5%
                suma_nivel = self.__evaluar_nivel_de_red_para_13(arbol_usuario, 1)
                depositar_monto_en_cuenta_de_usuario(usuario.id, obtener_x_porciento_de(suma_nivel, 5), plan_evaluando)
            if tipo_usuario_id == 6:
                # primer y segundo nivel, 5 y 2 % respectivamente
                x_ciento_nivel_uno = obtener_x_porciento_de(self.__evaluar_nivel_de_red_para_13(arbol_usuario, 1), 5)
                x_ciento_nivel_dos = obtener_x_porciento_de(self.__evaluar_nivel_de_red_para_13(arbol_usuario, 2), 2)
                depositar_monto_en_cuenta_de_usuario(usuario.id, x_ciento_nivel_uno + x_ciento_nivel_dos, plan_evaluando)
            if tipo_usuario_id == 7:
                # nivel uno, dos y tres, con % 5,2,2 respectivamente
                x_ciento_nivel_uno = obtener_x_porciento_de(self.__evaluar_nivel_de_red_para_13(arbol_usuario, 1), 5)
                x_ciento_nivel_dos = obtener_x_porciento_de(self.__evaluar_nivel_de_red_para_13(arbol_usuario, 2), 2)
                x_ciento_nivel_tres = obtener_x_porciento_de(self.__evaluar_nivel_de_red_para_13(arbol_usuario, 3), 2)
                depositar_monto_en_cuenta_de_usuario(usuario.id,
                                                     x_ciento_nivel_uno + x_ciento_nivel_dos + x_ciento_nivel_tres, plan_evaluando)
            if tipo_usuario_id == 8:
                # nivel uno, dos, tres y cuatro, con % 5,2,2,5 respectivamente
                x_ciento_nivel_uno = obtener_x_porciento_de(self.__evaluar_nivel_de_red_para_13(arbol_usuario, 1), 5)
                x_ciento_nivel_dos = obtener_x_porciento_de(self.__evaluar_nivel_de_red_para_13(arbol_usuario, 2), 2)
                x_ciento_nivel_tres = obtener_x_porciento_de(self.__evaluar_nivel_de_red_para_13(arbol_usuario, 3), 2)
                x_ciento_nivel_cuatro = obtener_x_porciento_de(self.__evaluar_nivel_de_red_para_13(arbol_usuario, 4), 5)
                depositar_monto_en_cuenta_de_usuario(usuario.id,
                                                     x_ciento_nivel_uno + x_ciento_nivel_dos + x_ciento_nivel_tres +
                                                     x_ciento_nivel_cuatro, plan_evaluando)


    def __evaluar_nivel_de_red_para_13(self, arbol_usuario, nivel):
        if nivel < 0:
            raise "NO puedo evaluar nivel de arbol menor que cero"
        if nivel == 0:
            return obtener_factura_total_de_usuario(arbol_usuario.raiz, only_plan=3)
        suma = 0.0
        nivel -= 1
        for sub_arbol in arbol_usuario.lista_subarboles:
            suma += self.__evaluar_nivel_de_red_para_13(sub_arbol, nivel)
        return suma

    """
    *****************************************************************************************************
    ***************************************PLAN DE COMPENSACION 14***************************************
    ***************************************PLAN DE COMPENSACION 14***************************************
    ***************************************PLAN DE COMPENSACION 14***************************************
    *****************************************************************************************************
    """
    def __evaluar_un_usuario_14(self, arbol_usuario):
        plan_evaluando = 14
        usuario = arbol_usuario.raiz
        tipo_usuario_id = usuario.perfilusuario.tipo_usuario.id
        if tipo_usuario_id > 4:
            if tipo_usuario_id == 4:
                # solo el nivel uno, y el 2%
                suma_nivel = self.__evaluar_nivel_de_red_para_14(arbol_usuario, 1)
                depositar_monto_en_cuenta_de_usuario(usuario.id, obtener_x_porciento_de(suma_nivel, 2), plan_evaluando)
            if tipo_usuario_id == 5:
                # solo el nivel uno, y el 5%
                suma_nivel = self.__evaluar_nivel_de_red_para_14(arbol_usuario, 1)
                depositar_monto_en_cuenta_de_usuario(usuario.id, obtener_x_porciento_de(suma_nivel, 5), plan_evaluando)
            if tipo_usuario_id == 6:
                # primer y segundo nivel, 5 y 2 % respectivamente
                x_ciento_nivel_uno = obtener_x_porciento_de(self.__evaluar_nivel_de_red_para_14(arbol_usuario, 1), 5)
                x_ciento_nivel_dos = obtener_x_porciento_de(self.__evaluar_nivel_de_red_para_14(arbol_usuario, 2), 2)
                depositar_monto_en_cuenta_de_usuario(usuario.id, x_ciento_nivel_uno + x_ciento_nivel_dos, plan_evaluando)
            if tipo_usuario_id == 7:
                # nivel uno, dos y tres, con % 5,2,2 respectivamente
                x_ciento_nivel_uno = obtener_x_porciento_de(self.__evaluar_nivel_de_red_para_14(arbol_usuario, 1), 5)
                x_ciento_nivel_dos = obtener_x_porciento_de(self.__evaluar_nivel_de_red_para_14(arbol_usuario, 2), 2)
                x_ciento_nivel_tres = obtener_x_porciento_de(self.__evaluar_nivel_de_red_para_14(arbol_usuario, 3), 2)
                depositar_monto_en_cuenta_de_usuario(usuario.id,
                                                     x_ciento_nivel_uno + x_ciento_nivel_dos + x_ciento_nivel_tres, plan_evaluando)
            if tipo_usuario_id == 8:
                # nivel uno, dos, tres y cuatro, con % 5,2,2,5 respectivamente
                x_ciento_nivel_uno = obtener_x_porciento_de(self.__evaluar_nivel_de_red_para_14(arbol_usuario, 1), 5)
                x_ciento_nivel_dos = obtener_x_porciento_de(self.__evaluar_nivel_de_red_para_14(arbol_usuario, 2), 2)
                x_ciento_nivel_tres = obtener_x_porciento_de(self.__evaluar_nivel_de_red_para_14(arbol_usuario, 3), 2)
                x_ciento_nivel_cuatro = obtener_x_porciento_de(self.__evaluar_nivel_de_red_para_14(arbol_usuario, 4), 5)
                depositar_monto_en_cuenta_de_usuario(usuario.id,
                                                     x_ciento_nivel_uno + x_ciento_nivel_dos + x_ciento_nivel_tres +
                                                     x_ciento_nivel_cuatro, plan_evaluando)


    def __evaluar_nivel_de_red_para_14(self, arbol_usuario, nivel):
        # print "Plan %s: Asignando ganancias..." % self.NUMERO_PLAN
        if nivel < 0:
            raise Exception("NO puedo evaluar un nivel de arbol menor que cero")
        if nivel == 0:
            return obtener_factura_total_de_usuario(arbol_usuario.raiz, only_plan=2)
        suma = 0.0
        nivel -= 1
        for sub_arbol in arbol_usuario.lista_subarboles:
            suma += self.__evaluar_nivel_de_red_para_14(sub_arbol, nivel)
        return suma

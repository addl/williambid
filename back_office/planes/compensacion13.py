# from back_office.banco import obtener_factura_total_de_usuario, depositar_monto_en_cuenta_de_usuario
# from back_office.planes.compensacion_12_13_14 import PlanCompensacion_12_13_14
# from back_office.util import obtener_x_porciento_de
#
# __author__ = 'bryan'
#
#
# class PlanCompensacionTrece(PlanCompensacionDoce):
#     """
#     Hereda del PLan 12, por lo que ejecuta el recorrido, y solo varia el origen de las ganancias
#     PLan unilevel BONO de IGUALACION
#     """
#
#     def __init__(self, arbol_gral):
#         print "Creating %s" % self.__class__
#         PlanCompensacionDoce.__init__(self, arbol_gral)
#         self.NUMERO_PLAN = 13
#
#
#     def __evaluar_nivel_de_red_para(self, arbol_usuario, nivel):
#         if nivel < 0:
#             raise "NO puedo evaluar nivel de arbol menor que cero"
#         if nivel == 0:
#             return obtener_factura_total_de_usuario(arbol_usuario.raiz, only_plan=3)
#         suma = 0.0
#         nivel -= 1
#         for sub_arbol in arbol_usuario.lista_subarboles:
#             suma += self.__evaluar_nivel_de_red_para(sub_arbol, nivel)
#         return suma








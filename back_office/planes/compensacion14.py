# from back_office.banco import obtener_factura_total_de_usuario, depositar_monto_en_cuenta_de_usuario
# from back_office.models import BancoUsuario
# from back_office.planes.compensacion_12_13_14 import PlanCompensacion_12_13_14
# from back_office.util import obtener_x_porciento_de
#
# __author__ = 'bryan'
#
#
# class PlanCompensacionCatorce(PlanCompensacion_12_13_14):
#     """
#     Este plan HEREDA del plan 12, ya que el esquema es el mismo solo cambia el origen del dinero
#     Es el 15 en el doc:
#     BONO DE IGUALACION DEL BINARIO HIBRIDO.
#     Ganaras un porcentaje del beneficio de las tus referidos directos y de algunas generaciones dependiendo tu rango:
#     """
#
#     def __init__(self, arbol_gral):
#         print "Creating %s" % self.__class__
#         PlanCompensacion_12_13_14.__init__(self, arbol_gral)
#         self.NUMERO_PLAN = 14
#
#     def __evaluar_nivel_de_red_para(self, arbol_usuario, nivel):
#         print "Plan %s: Asignando ganancias..." % self.NUMERO_PLAN
#         if nivel < 0:
#             raise Exception("NO puedo evaluar un nivel de arbol menor que cero")
#         if nivel == 0:
#             return obtener_factura_total_de_usuario(arbol_usuario.raiz, only_plan=2)
#         suma = 0.0
#         nivel -= 1
#         for sub_arbol in arbol_usuario.lista_subarboles:
#             suma += self.__evaluar_nivel_de_red_para(sub_arbol, nivel)
#         return suma
#
#     #def __obtener_ganancias_de_usuario_en_bono_1000(self, usuario):
#     #    cuenta = BancoUsuario.objects.get(usuario=usuario, tipo_plan=9)
#     #    return cuenta.monto_total

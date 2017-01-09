from django.contrib.auth.models import User
from back_office.models import Beneficios, UserXDeliveredProfit
from back_office.planes.compensacion10 import PlanCompensacionDiez
from back_office.planes.compensacion_12_13_14 import PlanCompensacion_12_13_14
from back_office.planes.compensacion2 import PlanCompensacionDos
from back_office.planes.compensacion3 import PlanCompensacionTres
from back_office.planes.compensacion9 import PlanCompensacionNueve
from back_office.planes.compensacion_general import PlanComponsacionGeneral
from back_office.planes.compensacion1 import PlanCompensacionUno
from back_office.planes.compensacion11 import PlanCompensacionOnce
from back_office.planes.compensacion4 import PlanCompensacionCuatro
from back_office.planes.compensacion5 import PlanCompensacionCinco
from back_office.planes.compensacion6 import PlanCompensacionSeis
from back_office.planes.compensacion7 import PlanCompensacionSiete
from back_office.planes.compensacion8 import PlanCompensacionOcho
from back_office.planes.utils import obtener_lista_de_usuarios
from back_office.tda.binario_hibrido import ArbolBinarioHibrido
from back_office.util import obtener_usuarios_mayor_a_basic
from back_office.tda.arbol_general import ArbolGeneral
from back_office.tda.heap import ArbolHeap
import logging

log = logging.getLogger(__name__)
__author__ = 'bryan'


class PlanesManagerSingleton():
    instance = None

    def get_instance():
        if not PlanesManagerSingleton.instance:
            log.info("Creando instancia de ManejadorPLanes")
            PlanesManagerSingleton.instance = PlanesManagerSingleton.__Manejador_Planes()
        # if not PlanesManagerSingleton.instance.is_alive():
        #    PlanesManagerSingleton.instance.start()
        log.info("Returning instance of ManejadorPlanes")
        return PlanesManagerSingleton.instance

    get_instance = staticmethod(get_instance)

    class __Manejador_Planes():

        def __init__(self):
            # Thread.__init__(self)
            try:
                lista_usuarios = obtener_lista_de_usuarios()
                # construir el arbol general
                self.arbol_general = self.construir_arbol_general(lista_usuarios=lista_usuarios)
                log.info("Arbol GENERAL creado, instance: %s " % self.arbol_general)
                # construir el arbol binario
                self.arbol_binario = self.construir_arbol_binario(obtener_usuarios_mayor_a_basic(), 0)
                log.info("Arbol BINARIO creado, instance: %s " % self.arbol_binario)
                # construir el binario hibrido
                self.arbol_binario_hibrido = self.construir_binario_hibrido(lista_usuarios=lista_usuarios)
                log.info("Arbol BINARIO-HIBRIDO creado, instance: %s " % self.arbol_binario_hibrido)
                # el plan 0 se encarga de actualizar el tipo de usuario
                self.plan_compensacion_general = PlanComponsacionGeneral(self.arbol_general, self.arbol_binario)
                self.__construir_planes_de_compensacion()
            except Exception, e:
                log.error(e.message)
                raise e

        def __construir_planes_de_compensacion(self):
            self.plan_compensacion_uno = PlanCompensacionUno(self.arbol_general)
            self.plan_compensacion_dos = PlanCompensacionDos(self.arbol_binario_hibrido)
            self.plan_compensacion_tres = PlanCompensacionTres(self.arbol_general)
            self.plan_compensacion_cuatro = PlanCompensacionCuatro(self.arbol_binario)
            self.plan_compensacion_cinco = PlanCompensacionCinco()
            self.plan_compensacion_seis = PlanCompensacionSeis()
            self.plan_compensacion_siete = PlanCompensacionSiete()
            self.plan_compensacion_ocho = PlanCompensacionOcho()
            self.plan_compensacion_nueve = PlanCompensacionNueve()
            self.plan_compensacion_diez = PlanCompensacionDiez()
            self.plan_compensacion_once = PlanCompensacionOnce()
            self.plan_compensacion_doce_trece_catorce = PlanCompensacion_12_13_14(self.arbol_general)
            # self.plan_compensacion_trece = PlanCompensacionTrece(self.arbol_general)
            # self.plan_compensacion_catorce = PlanCompensacionCatorce(self.arbol_general)

        def construir_arbol_general(self, lista_usuarios):
            # print "Construyendo arbol general ..."
            user_admin = User.objects.get(is_superuser=1)
            if not user_admin:
                log.error("No puedo crear el Plan No. 1. Usuario admin no encontrado")
                raise "No puedo crear el Plan No. 1. Usuario admin no encontrado"
            arbol_general = ArbolGeneral(user_admin)
            for user in lista_usuarios:
                padre = user.perfilusuario.padre.usuario
                arbol_padre = ArbolGeneral(padre)
                arbol_hijo = ArbolGeneral(user)
                arbol_general.adicionar_subarbol(arbol_padre, arbol_hijo)
                # print "Agregando Usuario %s, Padre es %s" % (user.id, padre.id)
            return arbol_general

        def construir_arbol_binario(self, lista_ordenada, pos):
            total = len(lista_ordenada)
            mitad = total / 2 - 1
            if pos > mitad:
                return ArbolHeap(lista_ordenada[pos])
            pos_izq = 2 * pos + 1
            pos_der = 2 * pos + 2
            raiz = lista_ordenada[pos]
            izq = None
            der = None
            # validamos posiciones
            if pos_izq < total:
                izq = self.construir_arbol_binario(lista_ordenada, pos_izq)
            if pos_der < total:
                der = self.construir_arbol_binario(lista_ordenada, pos_der)
            return ArbolHeap(raiz, izq, der)

        def construir_binario_hibrido(self, lista_usuarios):
            user_admin = User.objects.get(is_superuser=1)
            if not user_admin:
                log.error("No puedo crear el Plan No. 1. Usuario admin no encontrado")
                raise Exception("No puedo crear el Plan No. 1. Usuario admin no encontrado")
            binario_hibrido = ArbolBinarioHibrido(raiz=user_admin)
            for user in lista_usuarios:
                padre = user.perfilusuario.padre.usuario
                binario_hibrido.adicionar_usuario(user, padre)
            return binario_hibrido

        def registrar_usuario_a_planes_de_compensacion(self, usuario_nuevo, usuario_padre):
            if not usuario_padre:
                usuario_padre = User.objects.get(is_superuser=1)
            # adicionar el usuario al arbol general
            self.arbol_general.adicionar_subarbol(ArbolGeneral(usuario_padre), ArbolGeneral(usuario_nuevo))
            # para el arbol binario empresarial, tiene q ser miembro de 10 USD mensuales minimo
            if usuario_nuevo.perfilusuario.membresia.tipo_membresia.id > 0:
                # recostruimos el arbol binario para que contenga el nuevo usuario
                self.arbol_binario = self.construir_arbol_binario(obtener_usuarios_mayor_a_basic(), 0)
            # para el plan 5, es necesario ver si el padre cumple con los retos de agregar users
            PlanCompensacionCinco.computar_registro_de_usuario(usuario_nuevo, usuario_padre)
            # El plan de compensacion 2 se obvia y no se agrega al plan hibrido ya que no se cumplen las sgtes caracteristicas
            # 1. TENER UNA MEMBRESIA DE PAGO.
            # 2. TENER MINIMO DOS USUARIOS DIRECTOS EN TU RED.
            # 3. TENER MINIMO 50 PUNTOS

        def asignar_ganancias_a_usuarios(self):
            log.info("Asignando ganancias a usuarios en favor de cada plan...")
            self.plan_compensacion_uno.asignar_ganancia_a_cada_usuario() # okokokok
            resultados_hibrido = self.plan_compensacion_dos.asignar_ganancias_a_usuarios()  # okkkk
            # self.plan_compensacion_tres.evaluar_usuarios()
            self.plan_compensacion_cuatro.asignar_ganancia_a_usuarios()  # okkk

            # la funcion @cerrar_retos_vencidos_por_fecha del plan de compensacion 5....->
            # se encarga de llamar a la funcion correspondiente de asignar ganancias

            self.asignar_beneficios_usuarios_plan_6_7_8()  # okkk
            self.plan_compensacion_nueve.asignar_beneficios_usuarios()  # okkk
            # el plan de compensacion 10 corre una vez al dia, buscar ejecucion en archivo tasks
            # el plan de compensacion 11 de autoenriquecimiento, el cual cambia membresia automaticamente, debe correr una vez al dia

            # el plan 12, abarca el 13 y 14, para hacer un solo recorrido y evaluar los 3, ya que son parecidos
            self.plan_compensacion_doce_trece_catorce.evaluar_usuarios()

        def asignar_beneficios_usuarios_plan_6_7_8(self):
            beneficios = Beneficios.objects.filter(distribuido=0)
            for b in beneficios:
                # print 'Asignando beneficios pc ********** 6'
                self.plan_compensacion_seis.asignar_beneficios_usuarios(b.beneficio_total_empresa)
                self.plan_compensacion_siete.asignar_beneficio_total_empresa_socios_VIP_PRO(
                    b.beneficio_total_empresa_socios_VIP_PRO)
                self.plan_compensacion_ocho.asignar_beneficio_facturacion_global(b.facturacion_global)
                b.distribuido = True
                b.save(force_update=True)



        def execute_tasks(self):
            # asignar ganancias por plan, esta tarea corre normalmente una vez al mes
            self.asignar_ganancias_a_usuarios()
            # las ventas se tomaran a partir de la ultima fecha evaluada por los planes
            UserXDeliveredProfit.objects.create()


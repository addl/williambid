import datetime
from back_office.back_office_service_layer import es_usuario_ganador_de_reto, esta_usuario_participando_en_reto
from back_office.banco import depositar_monto_en_cuenta_de_usuario
from back_office.models import Reto, EstadoRetoUsuario, TipoReto
from back_office.planes.utils import evaluar_reto_uno
import logging

log = logging.getLogger(__name__)

__author__ = 'bryan'


class PlanCompensacionCinco():
    def __init__(self):
        log.info("Creating %s" % self.__class__)
        self.NUMERO_PLAN = 5

    # esta funcion corre en modo SHORT_PERIODICAL, y llama a asignar ganancias
    def cerrar_retos_vencidos_por_fecha(self):
        today = datetime.datetime.now()
        retos = Reto.objects.filter(tiempo__isnull=False, terminado=False)
        for reto in retos:
            fecha_limite = reto.tiempo
            if today >= fecha_limite:
                log.info("Plan %s cerrando reto %s" % (self.NUMERO_PLAN, reto.tipo_reto.descripcion))
                reto.terminado = True
                reto.save(force_update=True)
                self.__asignar_ganancias_a_usuario(reto)

    # esta funcion se llama siempre q se registre un usuario mediante
    # la funcion @registrar_usuario_a_planes_de_compensacion, en el manager planes
    def computar_registro_de_usuario(usuario_nuevo, usuario_padre):
        try:
            reto = Reto.objects.get(tipo_reto=TipoReto.objects.get(id=1), terminado=False)
            if reto is not None:
                if esta_usuario_participando_en_reto(usuario_padre, reto):
                    if reto.tipo_reto.id == 1:
                        evaluar_reto_uno(usuario_nuevo, usuario_padre, reto)
        except Exception, e:
            log.error(e.message)
            return

    computar_registro_de_usuario = staticmethod(computar_registro_de_usuario)

    # esta funcion es llamada desde el plan 11 AUTOENRIQUECIMIENTO, cuando existe un cambio de membresia
    # ******** OJO EL PLAN 11 CORRE UNA VEZ AL DIA *********
    def computar_cambio_de_membresia(usuario):
        log.info("Plan 5 computando cambio de membresia")
        usuario_padre = usuario.perfilusuario.padre.usuario
        try:
            reto = Reto.objects.get(tipo_reto=TipoReto.objects.get(id=2), terminado=False)
            # hay q validar si el cambio de membresia satisface la membresia del reto
            if usuario.perfilusuario.membresia_id >= reto.membresia_id:
                if esta_usuario_participando_en_reto(usuario_padre, reto):
                    if not es_usuario_ganador_de_reto(usuario_padre, reto):
                        estado_reto = EstadoRetoUsuario.objects.get(usuario=usuario_padre, reto=reto)
                        estado_reto.cantidad_personas = estado_reto.cantidad_personas + 1
                        if estado_reto.cantidad_personas >= reto.personas:
                            estado_reto.ganador = True
                        estado_reto.save(force_update=True)
        except Exception, e:
            log.error(e.message)
            return

    computar_cambio_de_membresia = staticmethod(computar_cambio_de_membresia)

    # *********************************************************
    # *****************PROBAR PARA VER COMO LO HACE************
    # *********************************************************
    def computar_venta_de_paquete_de_puja(venta_paquete_bid):
        usuario = venta_paquete_bid.en_red_de_usuario
        try:
            reto = Reto.objects.filter(tipo_reto=TipoReto.objects.get(id=3), terminado=False)
            if esta_usuario_participando_en_reto(usuario, reto):
                estado_reto = EstadoRetoUsuario.objects.get(usuario=usuario, reto=reto)
                estado_reto.dinero_paquetes_de_pujas = estado_reto.dinero_paquetes_de_pujas + venta_paquete_bid.preci
                if estado_reto.dinero_paquetes_de_pujas >= reto.dinero_pujas:
                    estado_reto.ganador = True
                estado_reto.save(force_update=True)
        except Exception, e:
            log.error(e.message)
            return

    computar_venta_de_paquete_de_puja = staticmethod(computar_venta_de_paquete_de_puja)

    # esta funcion es llamada por @self.cerrar_retos_vencidos_por_fecha, que corre en MODO SHORT PERIODICAL
    # y vela por cerrar los retos pasados de fecha
    def __asignar_ganancias_a_usuario(self, reto):
        log.info("Plan %s: RETOS de USUARIOS(BONOS DE LOGRO) - Asignando ganancias." % self.NUMERO_PLAN)
        estados_del_reto = EstadoRetoUsuario.objects.filter(reto=reto)
        for est_reto in estados_del_reto:
            user = est_reto.usuario
            # el estado de si un user es ganador o no, se determina en la funciones computar
            if est_reto.ganador:
                depositar_monto_en_cuenta_de_usuario(user.id, reto.dinero, self.NUMERO_PLAN)
        # eliminar todos los estados de retos y los ganadores
        estados_del_reto.delete()
        log.info("Plan %s Gananancias asignadas, eliminando estado de reto, para reto %s" % (
            self.NUMERO_PLAN, estados_del_reto))

    def __existen_retos_ahora(self):
        now = datetime.datetime.now()
        return len(Reto.objects.filter(tiempo__gte=now)) > 0

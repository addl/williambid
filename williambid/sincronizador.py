from datetime import datetime, timedelta
import random
from williambid.models import Subasta, Articulo, Venta, PaqueteBid, VentaPaqueteBid, VentaArticulo, AutoPuja, \
    SubastaVendida
from williambid.robot_manager import RobotManager
from williambid.service_layer import obtener_subastas_pujando, crear_subasta_de_valores_x_defecto, \
    verificar_que_articulo_no_este_en_puja, desactivar_subastas_vendidas, crear_subasta_de_paquete_de_bid, \
    pujar_subasta, \
    crear_subasta_vendida_a_partir_de_subasta
import logging

log = logging.getLogger(__name__)

__author__ = 'bryan'


class SincronizadorSingleInstance():
    instance = None

    def get_instance():
        if not SincronizadorSingleInstance.instance:
            log.info("Creando instancia de Sincronizador...")
            SincronizadorSingleInstance.instance = SincronizadorSingleInstance.__Sincronizador()
            # if not SincronizadorSingleInstance.instance.is_alive():
            # print "Sincronizador starting..."
            # SincronizadorSingleInstance.instance.start()

        log.info("Returning %s" % SincronizadorSingleInstance.instance)
        return SincronizadorSingleInstance.instance

    get_instance = staticmethod(get_instance)

    class __Sincronizador():

        MAXIMA_CANTIDAD_SUBASTAS = 9

        def __init__(self):
            log.info("Sincronizador inicializado...")
            self.robot_manager = RobotManager()
            self.autopujas_list = AutoPuja.objects.all()

        def _agregar_subastas_automaticamente(self):
            # buscar un articulo de subastas automaticas, aleatoriamente
            articulos = Articulo.objects.filter(pujas_automaticas=True)
            for articulo in articulos:
                band = False
                # si hay articulos en el stock
                if articulo.cantidad_de_articulos > 0:
                    # esto garantiza que ni las subastas activas ni las de espera representen al mismo articulo
                    if not verificar_que_articulo_no_este_en_puja(articulo.id):
                        log.info("Agregando al articulo %s automaticamente en subasta" % articulo)
                        # creamos la subasta y la guardamos en BD
                        subasta = crear_subasta_de_valores_x_defecto(articulo)
                        subasta.save(force_insert=True)
                        band = True
                if band:
                    break

        def _agregar_subasta_de_paquete_de_bids(self):
            if PaqueteBid.objects.count() > 0:
                paquete = random.choice(PaqueteBid.objects.all())
                subasta = crear_subasta_de_paquete_de_bid(paquete)
                subasta.save(force_insert=True)

        def existe_subasta_de_paquetes_de_bids(self):
            subastas_activas = Subasta.objects.filter(estado=Subasta.ACTIVE)
            for subasta in subastas_activas:
                if PaqueteBid.objects.filter(id=subasta.contenido.id):
                    return True
            return False

        def asignar_robots_a_subastas(self, subasta_id):
            log.info("Asignando robot a subasta desde Synchronizer")
            self.robot_manager.asignar_robot_a_subasta(subasta_id=subasta_id)

        # en cada iteracion o llamada a este metodo, pujar automaticamente 1 sola vez sobre cada articulo en subasta,
        # pero hay que tener en cuenta que si hay mas de un usuario con puja automatica sobre la misma subasta,
        # debe ser como una rueda, para que cada usuario puje rotativamente, de momento es random
        def autopujar_subastas(self):
            subastas_activas = Subasta.objects.filter(estado=Subasta.ACTIVE)
            for subasta in subastas_activas:
                autopujas_para_esta_subasta = AutoPuja.objects.filter(articulo=subasta.contenido).filter(
                    cantidad_pujas__gt=0).all()
                if subasta.ganador:
                    autopujas_para_esta_subasta = AutoPuja.objects.filter(articulo=subasta.contenido).exclude(
                        usuario=subasta.ganador)
                autopuja = random.choice(autopujas_para_esta_subasta) if len(autopujas_para_esta_subasta) > 0 else None
                if autopuja:
                    usuario = autopuja.usuario
                    if usuario.perfilusuario.cantidad_de_bids > 0 and autopuja.cantidad_pujas > 0:
                        log.info("Autopujando en subasta %s con usuario %s" % (subasta, usuario))
                        log.info("Autopujando en subasta %s con usuario %s" % (subasta, usuario))
                        # descontar bids al usuario
                        result = pujar_subasta(id_subasta=subasta.id, usuario=usuario)
                        if result:
                            # descontar bids al usuario
                            usuario.perfilusuario.cantidad_de_bids = usuario.perfilusuario.cantidad_de_bids - 1
                            usuario.perfilusuario.save(force_update=True)
                            # descontar bids a la autopuja
                            autopuja.cantidad_pujas = autopuja.cantidad_pujas - 1
                            autopuja.save(force_update=True)
                            # poner al tanto al sincronizador que asigna robots a la subasta
                            self.robot_manager.asignar_robot_a_subasta(subasta_id=subasta.id)
                            # self.robot_manager.cambiar_robots_ya_no_ganan_subasta(subasta_id=subasta.id)

        def verificar_subastas_terminadas(self):
            log.info("Verificando subastas terminadas**************")
            subastas = Subasta.objects.filter(estado=Subasta.ACTIVE)
            for subasta in subastas:
                now = datetime.now()
                fecha_exp = subasta.fecha_expiracion
                # print "Checkeando subastas terminadas...", now >= fecha_exp
                # preguntamos por un gganador, pq puede darse el caso q el usuario aggregue una subasta y cometa un
                # error en las fechas, las cuales pueden ser ya pasadas, en ese caso, no hay ganador
                if now >= fecha_exp and subasta.ganador:
                    log.info("Subasta terminada...")
                    # si expiro ya, la damos por terminada,
                    subasta.estado = Subasta.FINISHED
                    subasta.save(force_update=True)
                    # si la subasta termino, existe un ganador, y por tanto se debe registrar una venta
                    # registrar la venta en la base de datos siempre y cuando el ganador no sea un robot
                    if not subasta.gana_robot:
                        # asegurarnos de que no gano un robot
                        if not hasattr(subasta.ganador, 'robot'):
                            # agregar una subasta vendida y ponerla en el carrito del usuario
                            log.info("Aggregando subasta %s a carrito %s Ganador: %s" %
                                     (subasta, subasta.ganador.shoppinggcart, subasta.ganador))
                            subasta_vendida = crear_subasta_vendida_a_partir_de_subasta(subasta)
                            subasta_vendida.save(force_insert=True)
                            log.info("Registrando venta: %s - Precio: %s - Ganador: %s" %
                                     (subasta.contenido, subasta.precio_actual, subasta.ganador))
                            contenido = subasta.contenido
                            if contenido.articulo:
                                articulo = Articulo.objects.get(id=contenido.id)
                                venta_articulo = VentaArticulo(subasta=subasta_vendida, a_usuario=subasta.ganador,
                                                               articulo=articulo, precio=subasta.precio_actual)
                                venta_articulo.save(force_insert=True)
                                # si se agrego una venta este articulo debe disminuir la cantidad en stock
                                articulo.cantidad_de_articulos = articulo.cantidad_de_articulos - 1
                                articulo.save(force_update=True)
                            elif contenido.paquetebid:
                                paquete = PaqueteBid.objects.get(id=contenido.id)
                                venta_paquete = VentaPaqueteBid(subasta=subasta_vendida, a_usuario=subasta.ganador,
                                                                paquete=paquete, precio=subasta.precio_actual)
                                venta_paquete.save(force_insert=True)
                                # si se vendio un paquete de bid, hay q asignar los bids al usuario ganador,
                                # despues q pague

                    # y tambien dar por terminadas las que hayan vencido
                    # esto es util cuando el server se haya caido,
                    # de alguna forma debemos settear esas subastas que vencieron durante ese tiempo
                    desactivar_subastas_vendidas()

        def verificar_subastas_a_punto_de_terminar_sin_ganadores(self):
            """
                verificamos subastas cuyo tiempo de vida no supere el minuto y
                no tengan ganadores, entonces le asignamos robots
            """
            subastas = Subasta.objects.filter(estado=Subasta.ACTIVE, ganador=None)
            for p in subastas:
                now = datetime.now()
                fecha_exp = p.fecha_expiracion
                # los segundos y los minutos random, para no parecer que sean robot siempre al mismo tiempo
                seconds_random = random.randint(1, 55)
                minutes_random = random.randint(1, 7)
                now_mas_random_time = now + timedelta(minutes=minutes_random, seconds=seconds_random)
                if fecha_exp <= now_mas_random_time:
                    # print "Subasta %s a punto de terminar" % p
                    self.robot_manager.asignar_robot_a_subasta(p.id)

        def execute_tasks(self):
            log.info("Sinchronizer executing periodical tasks...")
            # verificar si hay subastas de paquetes de bids, sino agregar una
            # buscar paquete de bid y agregarlo a subasta en caso de que no existan subastas de paquetes
            if not self.existe_subasta_de_paquetes_de_bids():
                self._agregar_subasta_de_paquete_de_bids()
            # crear las subastas automaticamente en base de datos, si no hay 9
            if len(obtener_subastas_pujando()) < self.MAXIMA_CANTIDAD_SUBASTAS:
                # si hay al menos una subasta en cola, siempre debe de haber, pero hay q validar
                proximas_subastas = Subasta.objects.filter(estado=Subasta.WAITING)
                if len(proximas_subastas) > 0:
                    proxima_subasta = proximas_subastas[0]
                    proxima_subasta.estado = Subasta.ACTIVE
                    proxima_subasta.save(force_update=True)
            # agregar una subasta a la cola
            proximas_subastas = Subasta.objects.filter(estado=Subasta.WAITING)
            if len(proximas_subastas) < self.MAXIMA_CANTIDAD_SUBASTAS:
                self._agregar_subastas_automaticamente()
            # verificar la cantidad de robot
            self.robot_manager.crear_usuarios_robots()
            # liberar robots asignados a subastas que ya esten terminadas
            self.robot_manager.liberar_robots_de_subastas_terminadas()
            # que pasa si a determinadas subastas nadie les da pujar
            # a quien se venden???
            self.verificar_subastas_a_punto_de_terminar_sin_ganadores()

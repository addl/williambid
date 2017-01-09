from threading import Thread
import time, random

from django.contrib.auth.models import User
from datetime import datetime, timedelta

from williambid.killable_thread import KillableThread
from williambid.models import Subasta
from williambid.service_layer import pujar_subasta

__author__ = 'bryan'


class Robot(KillableThread):
    def __init__(self, id_robot, nickname, subasta_id, usuario_id):
        Thread.__init__(self)
        print "Inicializando robot %s, %s ..." % (id_robot, nickname)
        self.id_robot = id_robot
        self.nickname = nickname
        self.subasta = Subasta.objects.get(id=subasta_id)
        self.usuario_id = usuario_id
        # self.esta_ganando = False
        self.establecer_tiempo_de_pujar_subasta()
        self.start()

    def run(self):
        while True:
            # debemos actualizar la subasta que tiene el robot
            self.subasta = Subasta.objects.get(id=self.subasta.id)
            band = self.decidir_pujar()
            # print "La descision de pujar para bot %s es %s" % (self.nickname, band)
            if (band):
                print "Robot %s ha decidido pujar sobre %s, en el segundo %s" % (self.nickname, self.subasta, self.tiempo_aleatorio)
                self.pujar()
            time.sleep(5)

    def decidir_pujar(self):
        if not self.subasta.estado == Subasta.FINISHED:
            # si no es el(el robot), el que gana actualmente, pujamos
            if self.subasta.ganador.id != User.objects.get(id=self.usuario_id).id:
                # Si la subasta la gana un robot, hay que pujar siempre
                # hay que analizar si hay otros robots ganando, en ese caso, no se puja
                if self.subasta.gana_robot:
                    print "Pujando pq esta subasta (%s) la gana robot" % self.subasta
                    return True
                else:
                    # verificar si el usuario que va ganando la subasta tiene derecho a ganarla, por membresia
                    ganador = self.subasta.ganador
                    if ganador:
                        if ganador.perfilusuario.membresia.tipo_membresia.id < self.subasta.membresia_minima.id:
                            print "Pujando por membresia %s menor que %s" % \
                                  (ganador.perfilusuario.membresia.tipo_membresia.id, self.subasta.membresia_minima.id)
                            return True
                        # si la subasta la gana un usuario, garantizar que se llegue al precio definido en articulo o al paquete de bids
                        if self.subasta.contenido.articulo is not None:
                            if self.subasta.precio_actual < self.subasta.contenido.articulo.precio:
                                print "Pujando por precio minimo no alcanzado (%s<%s)" % \
                                      (self.subasta.precio_actual, self.subasta.contenido.articulo.precio)
                                return True
                        elif self.subasta.contenido.paquetebid:
                            if self.subasta.precio_actual < self.subasta.contenido.paquetebid.precio:
                                print "Pujando por precio minimo no alcanzado (%s<%s)" % \
                                      (self.subasta.precio_actual, self.subasta.contenido.paquetebid.precio)
                                return True
        return False

    def pujar(self):
        self.fecha_actual = datetime.now()
        fecha_exp = self.subasta.fecha_expiracion
        diffFecha = fecha_exp - self.fecha_actual
        # si el tiempo del robot ya paso, pujamos, el ordenador no dejara que esto suceda en mas de 2 seg,
        # a lo sumo, suposicion mia!!!, por tanto pujara casi en el mismo segundo que el establecio
        if diffFecha < self.tiempo_aleatorio:
            print "Robot %s, pujando en %s" % (self.nickname, self.subasta)
            # llamar la capa de servicios y mandar a pujar
            usuario = User.objects.get(id=self.usuario_id)
            self.subasta = pujar_subasta(self.subasta.id, usuario)
            # cambiamos el tiempo de pujar, para variar
            self.establecer_tiempo_de_pujar_subasta()

    def establecer_tiempo_de_pujar_subasta(self):
        # el numero aleatorio, establecemos un minimo, 5 en este caso
        # cuando el tiempo real sea menor que este numero, el robot pujara
        # esto comienza cuando alguien puje una subasta por 1ra vez, o por una autopuja
        self.fecha_actual = datetime.now()
        fecha_exp = self.subasta.fecha_expiracion
        diffFecha = fecha_exp - self.fecha_actual
        self.tiempo_aleatorio = timedelta(seconds=random.randrange(5, diffFecha.seconds))
        print "Robot %s ha establecido tiempo de pujar %s." % (self.nickname, self.tiempo_aleatorio)


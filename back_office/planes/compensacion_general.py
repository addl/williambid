from django.contrib.auth.models import User
from back_office.models import TipoUsuario, TipoMembresia
from back_office.planes.utils import analizar_membresias_directas, analizar_membresias_en_red, \
    analizar_por_propia_membresia, analizar_puntos
import logging

log = logging.getLogger(__name__)
__author__ = 'bryan'
# cada raiz del arbol guarda el id del usuario
# la raiz del arbol es el usuario admin de williambid

class PlanComponsacionGeneral():
    arbol_general = None
    arbol_binario = None
    NUMERO_PLAN = 0

    def __init__(self, arbol_general, arbol_binario):
        log.info("Creating %s" % self.__class__)
        self.arbol_general = arbol_general
        self.arbol_binario = arbol_binario

    def actualizar_puntacion_de_usuarios(self):
        recorrido = {}
        self.__buscar_puntacion_de_usuarios(self.arbol_general, len(TipoMembresia.objects.all()), recorrido)
        for id_user, ptos in recorrido.items():
            user = User.objects.get(id=id_user)
            user.perfilusuario.cantidad_de_puntos = ptos
            user.perfilusuario.save(force_update=True)
        print recorrido

    def __buscar_puntacion_de_usuarios(self, arbol_gral, cant_tipo_membresias, mapa_recorrido):
        log.info("PLan %s, analizando puntuacion de usuarios" % self.NUMERO_PLAN)
        puntos_mem_directa = list()
        cantidad_de_junior = 0
        for i in range(cant_tipo_membresias):
            puntos_mem_directa.append(0)
        if arbol_gral.es_hoja():
            return cantidad_de_junior
        else:
            for sub_arbol in arbol_gral.lista_subarboles:
                id_mem = sub_arbol.raiz.perfilusuario.membresia.id
                puntos_mem_directa[id_mem - 1] = puntos_mem_directa[id_mem - 1] + 1
                cantidad_de_junior += self.__buscar_puntacion_de_usuarios(sub_arbol, cant_tipo_membresias, mapa_recorrido)
        # asignar la cantidad de puntos a este usuario
        total_ptos = self.__evaluar_puntos_para_usuario(arbol_gral, puntos_mem_directa, cantidad_de_junior)
        mapa_recorrido[arbol_gral.raiz.id] = total_ptos
        log.info("PLan %s, Terminado analisis de puntuacion de usuarios" % self.NUMERO_PLAN)
        return cantidad_de_junior + puntos_mem_directa[1]

    # buscar esto de los puntos
    def __evaluar_puntos_para_usuario(self, arbol_usuario, red_directa, juniors_en_red):
        usuario = arbol_usuario.raiz
        puntuacion_total = red_directa[0] * 1 + red_directa[1] * 10 + red_directa[2] * 20 \
                           + red_directa[3] * 30 + red_directa[4] * 50 + red_directa[5] * 100 \
                           + red_directa[6] * 200 + red_directa[7] * 300 + red_directa[8] * 500
        factor_jnr = 1
        if usuario.perfilusuario.membresia.id == 3:
            factor_jnr = 2
        if usuario.perfilusuario.membresia.id == 4:
            factor_jnr = 3
        if usuario.perfilusuario.membresia.id == 5:
            factor_jnr = 5
        if usuario.perfilusuario.membresia.id == 6:
            factor_jnr = 10
        if usuario.perfilusuario.membresia.id == 7:
            factor_jnr = 20
        if usuario.perfilusuario.membresia.id == 8:
            factor_jnr = 30
        if usuario.perfilusuario.membresia.id == 9:
            factor_jnr = 50
        puntuacion_total += juniors_en_red * factor_jnr
        return puntuacion_total


    #ver como usar este recorrido para actualizar satus de todosl los user
    def actualizar_tipo_usuario_para_cada_usuario(self):
        log.info("Plan %s: Recorrido, actualizar tipo de usuario para cada usuario." % self.NUMERO_PLAN)
        cola = []
        # recorrido = []
        cola.append(self.arbol_general)
        while len(cola) > 0:
            frente = cola.__getitem__(0)
            cola.remove(frente)
            tipo_usuario = self.__analizar_tipo_usuario_para_usuario(frente)
            usuario = frente.raiz
            # ignoramos al usuario admin(EMPRESA), ya que hay que darle la maxima prioridad
            if usuario.perfilusuario.tipo_usuario.id != tipo_usuario.id and not usuario.is_superuser:
                print "Usuario %s con tipo de usuario %s, cambiando a tipo de usuario: %s" % \
                      (usuario, usuario.perfilusuario.tipo_usuario.nombre, tipo_usuario.nombre)
                usuario.perfilusuario.tipo_usuario = tipo_usuario
                usuario.perfilusuario.save(force_update=True)
            # recorrido.append(frente.raiz)
            for sub_arbol in frente.lista_subarboles:
                cola.append(sub_arbol)
        log.info("Plan %s: Recorrido para tipo de usuario finalizado" % self.NUMERO_PLAN)
        return True

    def __analizar_tipo_usuario_para_usuario(self, arbol_general_usuario):
        # primero analizamos por cantidad de puntos
        min_tipo_usuario = analizar_puntos(arbol_general_usuario)
        # por membresias directa en tu red
        tipo_usuario_mem_directa = analizar_membresias_directas(arbol_general_usuario)
        if tipo_usuario_mem_directa.id > min_tipo_usuario.id:
            min_tipo_usuario = tipo_usuario_mem_directa
        # por membresias en toda tu red, partiendo de ti hacia abajo
        tipo_usuario_mem_en_red = analizar_membresias_en_red(arbol_general_usuario)
        if tipo_usuario_mem_en_red.id > min_tipo_usuario.id:
            min_tipo_usuario = tipo_usuario_mem_en_red
        # por la membresia propia del usuario
        tipo_usuario_mem_propia = analizar_por_propia_membresia(arbol_general_usuario)
        if tipo_usuario_mem_propia.id > min_tipo_usuario.id:
            min_tipo_usuario = tipo_usuario_mem_en_red
        return min_tipo_usuario



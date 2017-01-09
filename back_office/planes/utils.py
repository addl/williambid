from django.contrib.auth.models import User
from django.conf import settings

from back_office.back_office_service_layer import es_usuario_ganador_de_reto
from back_office.models import TipoUsuario, EstadoRetoUsuario


def analizar_membresias_directas(arbol_gral_usuario):
    su_red = arbol_gral_usuario.lista_subarboles
    cant_pro = 0
    cant_player = 0
    cant_player_pro = 0
    cant_vip = 0
    for arbol_miembro in su_red:
        miembro = arbol_miembro.raiz
        id_tipo_mem = miembro.perfilusuario.membresia.tipo_membresia.id
        if id_tipo_mem == 5:
            cant_pro += 1
        if id_tipo_mem == 6:
            cant_player += 1
        if id_tipo_mem == 7:
            cant_player_pro += 1
        if id_tipo_mem == 8:
            cant_vip += 1
    # determinar el tipo de usuario partiendo de mayor a menor
    if cant_pro >= 500 or cant_player >= 300 or cant_player_pro > 200 or cant_vip > 100:
        return TipoUsuario.objects.get(id=8)
    if cant_pro >= 300 or cant_player >= 200 or cant_player_pro > 100 or cant_vip > 50:
        return TipoUsuario.objects.get(id=7)
    if cant_pro >= 200 or cant_player >= 100 or cant_player_pro > 50 or cant_vip > 30:
        return TipoUsuario.objects.get(id=6)
    if cant_pro >= 100 or cant_player >= 50 or cant_player_pro > 35 or cant_vip > 20:
        return TipoUsuario.objects.get(id=5)
    if cant_pro >= 50 or cant_player >= 30 or cant_player_pro > 20 or cant_vip > 10:
        return TipoUsuario.objects.get(id=4)
    if cant_pro >= 30 or cant_player >= 20 or cant_player_pro > 10 or cant_vip > 6:
        return TipoUsuario.objects.get(id=3)
    if cant_pro >= 15 or cant_player >= 10 or cant_player_pro > 5 or cant_vip > 3:
        return TipoUsuario.objects.get(id=2)
    return TipoUsuario.objects.get(id=1)


def analizar_por_propia_membresia(arbol_gral_usuario):
    usuario = arbol_gral_usuario.raiz
    registro_de_pagos = 4
    if usuario.perfilusuario.membresia.tipo_membresia.id == 9 and registro_de_pagos > 2:
        return TipoUsuario.objects.get(id=8)
    if usuario.perfilusuario.membresia.tipo_membresia.id == 8 and registro_de_pagos > 2:
        return TipoUsuario.objects.get(id=7)
    if usuario.perfilusuario.membresia.tipo_membresia.id == 7 and registro_de_pagos > 2:
        return TipoUsuario.objects.get(id=6)
    if usuario.perfilusuario.membresia.tipo_membresia.id == 6 and registro_de_pagos > 2:
        return TipoUsuario.objects.get(id=5)
    if usuario.perfilusuario.membresia.tipo_membresia.id == 5 and registro_de_pagos > 2:
        return TipoUsuario.objects.get(id=4)
    if usuario.perfilusuario.membresia.tipo_membresia.id == 4 and registro_de_pagos > 2:
        return TipoUsuario.objects.get(id=3)
    if usuario.perfilusuario.membresia.tipo_membresia.id == 3 and registro_de_pagos > 2:
        return TipoUsuario.objects.get(id=2)
    return TipoUsuario.objects.get(id=1)

def analizar_membresias_en_red(arbol_gral_usuario):
    res = buscar_cantidades_de_membresias_en_red(arbol_gral_usuario)
    cant_pro = res[0]
    cant_player_pro = res[1]
    cant_vip_winner = res[2]
    if cant_pro >= 1000 or cant_player_pro >= 750 or cant_vip_winner >= 300:
        return TipoUsuario.objects.get(id=8)
    if cant_pro >= 750 or cant_player_pro >= 500 or cant_vip_winner >= 200:
        return TipoUsuario.objects.get(id=7)
    if cant_pro >= 500 or cant_player_pro >= 300 or cant_vip_winner >= 100:
        return TipoUsuario.objects.get(id=6)
    if cant_pro >= 250 or cant_player_pro >= 150 or cant_vip_winner >= 50:
        return TipoUsuario.objects.get(id=5)
    if cant_pro >= 150 or cant_player_pro >= 75 or cant_vip_winner >= 25:
        return TipoUsuario.objects.get(id=4)
    if cant_pro >= 100 or cant_player_pro >= 50 or cant_vip_winner >= 30:
        return TipoUsuario.objects.get(id=3)
    if cant_pro >= 50 or cant_player_pro >= 25 or cant_vip_winner >= 15:
        return TipoUsuario.objects.get(id=2)
    return TipoUsuario.objects.get(id=1)

def buscar_cantidades_de_membresias_en_red(arbol_gral_usuario):
    """
    # devuelve una la lista de indicadores, manejarla con cuidado, contendra en la 1ra pos: cant profesional, 2da: player-pro y 3ra: vip_winners
    """
    cant_pro = 0
    cant_player_pro = 0
    cant_vip_winner = 0
    if (arbol_gral_usuario.es_hoja()):
        return [0, 0, 0]
    else:
        for arbol in arbol_gral_usuario.lista_subarboles:
            tipo_mem_id = arbol.raiz.perfilusuario.membresia.tipo_membresia.id
            if tipo_mem_id == 5:  # si es profesional
                cant_pro += 1
            if tipo_mem_id == 7:  # si es player pro
                cant_player_pro += 1
            if tipo_mem_id == 9:  # si es VIP winner
                cant_vip_winner += 1
            res = buscar_cantidades_de_membresias_en_red(arbol)
            cant_pro += res[0]
            cant_player_pro += res[1]
            cant_vip_winner += res[2]
    # retornamos la lista
    return [cant_pro, cant_player_pro, cant_vip_winner]


def analizar_puntos(usuario_arbol_gral):
    usuario = usuario_arbol_gral.raiz
    cant_ptos = usuario.perfilusuario.cantidad_de_puntos
    if cant_ptos > 999 and cant_ptos <= 2000:
        return TipoUsuario.objects.get(id=2)
    if cant_ptos > 2000 and cant_ptos <= 5000:
        return TipoUsuario.objects.get(id=3)
    if cant_ptos > 5000 and cant_ptos <= 10000:
        return TipoUsuario.objects.get(id=4)
    if cant_ptos > 10000 and cant_ptos <= 20000:
        return TipoUsuario.objects.get(id=5)
    if cant_ptos > 20000 and cant_ptos <= 30000:
        return TipoUsuario.objects.get(id=6)
    if cant_ptos > 30000 and cant_ptos <= 50000:
        return TipoUsuario.objects.get(id=7)
    if cant_ptos > 50000:
        return TipoUsuario.objects.get(id=8)
    # si los ptos no son sufiientes para ninguno de los anteriores, then default
    return TipoUsuario.objects.get(id=1)


def evaluar_reto_uno(usuario_nuevo, usuario_padre, reto):
    if not es_usuario_ganador_de_reto(usuario_padre, reto):
        if usuario_nuevo.perfilusuario.membresia.id >= reto.membresia.id:
            estado_reto = EstadoRetoUsuario.objects.get(usuario=usuario_padre, reto=reto)
            estado_reto.cantidad_personas = estado_reto.cantidad_personas + 1
            if estado_reto.cantidad_personas >= reto.personas:
                estado_reto.ganador = True
            estado_reto.save(force_update=True)


def obtener_lista_de_usuarios(exclude_admin=True):
    BOTS_ON_TREE = getattr(settings, 'BOTS_ON_TREE', False)
    print "Obtainig BOTS_ON_TREE %s" % BOTS_ON_TREE
    user_query = User.objects.filter(is_active=1)
    if exclude_admin:
        user_query = user_query.exclude(is_superuser=1)
    if BOTS_ON_TREE:
        # devolvemos todos los usuarios, incluyendo los bots
        return user_query
    # excluimos aquellos usuarios que tienen un robot, los bots
    return user_query.exclude(robot__isnull=False)

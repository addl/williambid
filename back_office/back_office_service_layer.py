import datetime
from django.contrib.auth.models import User
from back_office.models import BancoUsuario, Reto, EstadoRetoUsuario

__author__ = 'bryan'


def inscribir_usuario_en_reto(usuario, reto_id):
    EstadoRetoUsuario.objects.create(usuario=usuario, reto=Reto.objects.get(id=reto_id))


def obtener_retos():
    return Reto.objects.filter()


def es_usuario_ganador_de_reto(usuario, reto):
    band = False
    try:
        band = EstadoRetoUsuario.objects.get(usuario=usuario, reto=reto).ganador
    except:
        return False
    return band


def esta_usuario_participando_en_reto(usuario, reto):
    estado = None
    try:
        estado = EstadoRetoUsuario.objects.get(usuario=usuario, reto=reto)
    except:
        return False

    return True if estado else False


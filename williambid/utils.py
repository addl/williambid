import json
import os
import random
from django.contrib.auth.models import User
from django.core import serializers
from django.conf import settings
from back_office.models import PerfilUsuario, Membresia, TipoUsuario
from williambid.models import Robot, ShoppinggCart

import logging
log = logging.getLogger(__name__)

VOCALES = ("a", "e", "i", "o", "u")
CONSONANTES = ("b", "c", "d", "f", "h", "j", "k", "l", "m", "r", "v", "g", "t")


def obtener_subasta_formato_json(subasta):
    # es mandatorio serializar SOLO los campos que se usan en el cliente
    # de otro modo se podrian ver campos como gana robot, precio minimo, etc
    # serialize requiere un iterable, solo queremos un objeto
    subasta_json = serializers.serialize('json', [subasta],
                                      fields=("precio_actual", "fecha_expiracion", "terminada", "ganador"),
                                      use_natural_foreign_keys=True)
    return json.loads(subasta_json)[0]

def obtener_user_formato_json(user):
    dict_user = {}
    dict_user['username'] = user.username
    dict_user['email'] = user.email
    dict_user['membresia'] = user.perfilusuario.membresia.tipo_membresia.nombre
    dict_user['provincia'] = user.perfilusuario.provincia
    dict_user['pais'] = user.perfilusuario.pais
    dict_user['telefono'] = user.perfilusuario.telefono
    dict_user['skype'] = user.perfilusuario.skype_id
    dict_user['whatsapp'] = user.perfilusuario.whatsapp_id

    # usrjson = serializers.serialize('json', [user], fields=('username', 'firstname', 'email', 'perfilusuario'))
    #return json.loads(usrjson)[0]
    return dict_user


def generar_simple_nick(caracteres):
    nick = ""
    for i in range(0, caracteres):
        if i % 2 == 0:
            nick = nick + random.choice(CONSONANTES)
        else:
            nick = nick + random.choice(VOCALES)
    return nick


def registrar_usuario(form, user_from=None):
    # creamos el usuario
    usuario = User()
    try:
        usuario.username = form.clean_username()
        # usamos el metodo apropiado del objeto usuario para encryptar el passs
        # de lo contrario cuando te autenticas falla, asi pongas la correcta
        usuario.set_password(form.clean_password2())
        usuario.email = form.cleaned_data['email']
        usuario.save(force_insert=True)  # por si acaso, forzamos
        # le creamos un carrito de compra
        carrito = ShoppinggCart()
        carrito.usuario = usuario
        carrito.save(force_insert=True)
        # creamos el perfil del usuario
        perfil_usuario = PerfilUsuario()
        perfil_usuario.usuario = usuario
        if not user_from:
            # asignamos un padre al usuario
            user_from = User.objects.get(is_superuser=True)
        print "Asignando a usuario %s su papa, %s" % (usuario.username, user_from)
        perfil_usuario.padre = user_from.perfilusuario
        # buscar la membresia correspondiente y asignarla al perfil
        # empezando por 1, free, 2 bronce, 3, plata, etc....
        membresia = Membresia.objects.get(id=1)
        perfil_usuario.membresia = membresia
        tipousuario = TipoUsuario.objects.get(id=1)
        perfil_usuario.tipo_usuario = tipousuario
        perfil_usuario.seudonimo = form.cleaned_data['seudonimo']
        perfil_usuario.ciudad = form.cleaned_data['ciudad']
        perfil_usuario.direccion = form.cleaned_data['direccion']
        perfil_usuario.pais = form.cleaned_data['pais']
        perfil_usuario.provincia = form.cleaned_data['provincia']
        perfil_usuario.telefono = form.cleaned_data['telefono']
        perfil_usuario.skype_id = form.cleaned_data['skype_id']
        perfil_usuario.whatsapp_id = form.cleaned_data['whatsapp_id']
        # agregamos a la base de datos
        perfil_usuario.save(force_insert=True)
        print "Agregados Usuario y Perfil a la BD..."
    except Exception, e:
        print "Exception in register user %s " % e
        print "Ha ocurrido un error en el registro %s." % e.message
        return usuario
    return usuario

def actualizar_perfil_de_usuario(form, usuario):
    try:
        # usuario.username = form.clean_username()
        # usamos el metodo apropiado del objeto usuario para encryptar el passs
        # de lo contrario cuando te autenticas falla, asi pongas la correcta
        usuario.set_password(form.clean_password2())
        usuario.email = form.cleaned_data['email']
        usuario.save(force_insert=True)  # por si acaso, forzamos
        # creamos el perfil del usuario
        perfil_usuario = usuario.perfilusuario
        perfil_usuario.seudonimo = form.cleaned_data['seudonimo']
        perfil_usuario.ciudad = form.cleaned_data['ciudad']
        perfil_usuario.direccion = form.cleaned_data['direccion']
        perfil_usuario.pais = form.cleaned_data['pais']
        perfil_usuario.provincia = form.cleaned_data['provincia']
        perfil_usuario.telefono = form.cleaned_data['telefono']
        perfil_usuario.skype_id = form.cleaned_data['skype_id']
        perfil_usuario.whatsapp_id = form.cleaned_data['whatsapp_id']
        # agregamos a la base de datos
        perfil_usuario.save(force_insert=True)
        print "Agregados Usuario y Perfil a la BD..."
    except Exception, e:
        print "Exception in register user %s " % e
        print "Ha ocurrido un error en el registro %s." % e.message
        return usuario
    return usuario


class OnlineUsers():

    latest_users_online = 500

    def obtener_usuarios_online():
        real_users = User.objects.filter(is_staff=True).count()
        robot_count = Robot.objects.count()
        rate_count = random.randint(-100, 200)
        OnlineUsers.latest_users_online = int(real_users + robot_count + rate_count + OnlineUsers.latest_users_online)
        return OnlineUsers.latest_users_online

    obtener_usuarios_online = staticmethod(obtener_usuarios_online)


def findPlansFileDescriptorByLocale(locale_as_str):
    url_to_file = os.path.join(settings.BASE_DIR, "static/files/plan_%s.pdf" % locale_as_str)
    log.info("Downloading Plan Descriptor from %s" % url_to_file)
    if os.path.isfile(url_to_file):
        return open(url_to_file, "r")
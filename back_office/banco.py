from datetime import datetime
from back_office.models import BancoUsuario, HistorialTransacciones
from django.contrib.auth.models import User
import logging

log = logging.getLogger(__name__)
__author__ = 'bryan'


def depositar_monto_en_cuenta_de_usuario(miembro_id, monto_de_usuario, numero_plan):
    usuario_miembro = User.objects.get(id=miembro_id)
    if not monto_de_usuario > 0.0:
        return
    log.info("BANCO WILLIAM depositando ganancias a usuario %s con monto %s en el plan %s" % (
        usuario_miembro, monto_de_usuario, numero_plan))
    # le ponemos el dinero en el banco de williambid
    cuenta = None
    try:
        cuenta = BancoUsuario.objects.get(usuario=usuario_miembro, tipo_plan=numero_plan)
    except Exception, e:
        pass
    if not cuenta:
        cuenta = BancoUsuario(usuario=usuario_miembro, tipo_plan=numero_plan, monto_total=0)
        cuenta.save(force_insert=True)
    saldo_anterior = cuenta.monto_total
    crecimiento = monto_de_usuario
    cuenta.monto_total += crecimiento
    cuenta.save(force_update=True)
    # HistorialTransacciones.objects.create(cuenta=cuenta, cantidad=0, deposito=crecimiento, fecha=datetime.now())


def extaer_dinero_de_la_cuenta_de_usuario(miembro_id, cantidad):
    cuentas = User.objects.get(id=miembro_id).bancousuario_set.all()
    for cuenta in cuentas:
        if cuenta.monto_total >= cantidad:
            cuenta.monto_total -= cantidad
            cuenta.save(force_update=True)
            # HistorialTransacciones.objects.create(cuenta=cuenta, cantidad=cantidad, deposito=0, fecha=datetime.now())
        else:
            cantidad -= cuenta.monto_total
            cuenta.monto_total = 0
            cuenta.save(force_update=True)
            # HistorialTransacciones.objects.create(cuenta=cuenta, cantidad=cuenta.monto_total, deposito=0, fecha=datetime.now())


def obtener_factura_total_de_usuario(usuario, except_plan=0, only_plan=0):
    cuentas = usuario.bancousuario_set.all()
    if except_plan != 0 and only_plan != 0:
        log.error("Puedo calcular solo except_plan o only_plan, no los dos a la vez")
        raise "Puedo calcular solo except_plan o only_plan, no los dos a la vez"
    if except_plan != 0:
        cuentas = BancoUsuario.objects.filter(usuario=usuario).exclude(tipo_plan=except_plan)
    if only_plan != 0:
        cuentas = BancoUsuario.objects.filter(usuario=usuario, tipo_plan=only_plan)
    suma = 0
    for cuenta in cuentas:
        suma += cuenta.monto_total
    return suma

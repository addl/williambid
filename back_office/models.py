from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
# Create your models here.
from easymode.i18n.decorators import I18n


class TipoMembresia(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Membresia(models.Model):
    tipo_membresia = models.OneToOneField(TipoMembresia)
    numero_bids_mensuales = models.IntegerField(default=0)
    posibilidad_pack_anual_con_descuento = models.BooleanField(default=True)
    accionista_de_empresa = models.BooleanField(default=True)
    precio = models.FloatField(default=0)

    def __str__(self):
        return self.tipo_membresia.nombre


class TipoUsuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User)
    # researching many to many wit
    padre = models.ForeignKey('self', related_name='hijos', null=True)
    # datos del perfil
    tipo_usuario = models.ForeignKey(TipoUsuario, editable=False, default=1)
    membresia = models.ForeignKey(Membresia, null=False)
    fecha_obtuvo_membresia = models.DateTimeField(auto_now=True)
    direccion = models.TextField(blank=False)
    ciudad = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    telefono = models.TextField()
    seudonimo = models.CharField(unique=True, max_length=100)
    whatsapp_id = models.CharField(max_length=100)
    skype_id = models.CharField(max_length=100)
    # Util para el sistema
    cantidad_de_puntos = models.IntegerField(default=0)
    cantidad_de_bids = models.IntegerField(default=0)


class BancoUsuario(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User)
    tipo_plan = models.IntegerField(default=0, null=False)
    monto_total = models.FloatField(default=0)


class HistorialTransacciones(models.Model):
    cuenta = models.ForeignKey(BancoUsuario)
    cantidad = models.FloatField()
    deposito = models.BooleanField(default=False)
    fecha = models.DateTimeField(auto_now=True)


class Mensaje(models.Model):
    de_usuario = models.ForeignKey(User, null=False, related_name='sender')
    para_usuario = models.ForeignKey(User, null=False, related_name='receiver')
    mensaje = models.TextField(null=False)
    leido = models.BooleanField(default=False)
    fecha_enviado = models.DateTimeField(auto_now=True)


class Invitacion(models.Model):
    de_usuario = models.ForeignKey(User)
    para = models.CharField(max_length=50)
    para_correo = models.EmailField()
    url = models.URLField()


class TipoReto(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.TextField(default="Descripcion de tipo de reto")

    def __str__(self):
        return self.descripcion


class Reto(models.Model):
    id = models.AutoField(primary_key=True)
    tipo_reto = models.ForeignKey(TipoReto)
    personas = models.IntegerField(null=True, blank=True)
    membresia = models.ForeignKey(TipoMembresia, null=True, blank=True)
    tiempo = models.DateTimeField(null=True, blank=True)
    dinero_pujas = models.FloatField(null=True, default=0, blank=True)
    dinero = models.FloatField()
    terminado = models.BooleanField(default=False, editable=False)
    cerrado = models.BooleanField(default=False, editable=False)

    def __str__(self):
        return self.tipo_reto.descripcion


class EstadoRetoUsuario(models.Model):
    id = models.AutoField(primary_key=True)
    reto = models.ForeignKey(Reto)
    usuario = models.ForeignKey(User)
    cantidad_personas = models.IntegerField(default=0, null=True)
    dinero_paquetes_de_pujas = models.FloatField(default=0, null=True)
    cantidad_de_paquetes_de_pujas = models.IntegerField(default=0, null=True)
    ganador = models.BooleanField(default=False)


class PlanCompensacion(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    num_plan = models.IntegerField()
    title = models.CharField(max_length=50)
    descripcion = models.TextField()
    requisito = models.BooleanField(default=True,
                                    help_text="Marque esta casilla si existe algun requisito para cobrar este plan")
    # requisitos para cobrar el plan
    tipo_usuario = models.ForeignKey(TipoUsuario, null=True, default=1)
    membresia_minima = models.ForeignKey(TipoMembresia, null=True, default=1)
    cantidad_de_usuarios_en_red = models.IntegerField(null=True, default=0)
    cantidad_de_dinero = models.FloatField(null=True, default=0)
    cantidad_de_puntos = models.IntegerField(null=True, default=0)

    def __str__(self):
        return "Plan de compensacion: %s" % self.num_plan


# Plan de compensacion 6,7,8
class Beneficios(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    beneficio_total_empresa = models.IntegerField(
        help_text='Beneficio total de la empresa que se repartira mensualmente un 1% a todos los socios con membresias de pago')
    beneficio_total_empresa_socios_VIP_PRO = models.IntegerField(
        help_text='Beneficio total de la empresa que se repartira mensualmente un 2% a todos los socios con membresis de pago')
    facturacion_global = models.IntegerField(
        help_text='Se repartira un 3% de la facturacion global entre las personas que alcancen una facturacion en toda su red superior a 100.000 usd')
    distribuido = models.BooleanField(editable=False, default=False)

    def __str__(self):
        return "Beneficios %s" % self.id


class AdvertisementTool(models.Model):
    title = models.CharField(max_length=200)
    # user = models.ForeignKey(User)
    description = models.TextField()
    tool_file = models.FileField(upload_to='static/tools/%Y/%m/%d')
    # tool_file = models.FileField(upload_to='static/tools')


# para guardar la ultima fecha de asignacion de ganancias por los planes de compensacion
class UserXDeliveredProfit(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    date = models.DateTimeField(null=False, auto_now_add=True)


# para guardar las transacciones de paypal y checkear la  cantidad cuando retorne desde paypal
class WilliamPaypalTransaction(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey(User)
    amount = models.FloatField(null=False)


class PackageTransaction(WilliamPaypalTransaction):
    pkt_id = models.IntegerField(null=False)


class ShoppingCartTransaction(WilliamPaypalTransaction):
    cart_id = models.IntegerField(null=False)

import os
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime, timedelta
from back_office.models import Membresia, TipoMembresia
from william.settings import *


# for internazionalization


# Create your models here.
class TipoSubasta(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


from easymode.i18n.decorators import I18n


@I18n('nombre', 'descripcion')
class Content(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Articulo(Content):
    imagen = models.ImageField(upload_to='static/media/img/articulos/%Y/%m/%d', default='static/img/nimage.jpeg')
    cantidad_de_articulos = models.IntegerField(help_text="Cantidad de articulos en stock")
    precio = models.FloatField(help_text="Defina un precio para el cual Ud. considera tener ganancia minima")
    pujas_automaticas = models.BooleanField(default=False,
                                            help_text="Marque esta casilla si Ud desea que este articulo entre automaticamente en subasta")

    def __str__(self):
        return self.nombre


class PaqueteBid(Content):
    cantidad_de_bids = models.IntegerField(help_text="Cantidad de bids que tendra el paquete")
    precio = models.FloatField(help_text="Defina un precio para el cual Ud. considera tener ganancia minima")

    def __str__(self):
        return self.cantidad_de_bids.__str__() + ', ' + self.precio.__str__()


class Subasta(models.Model):
    WAITING = 1
    ACTIVE = 2
    FINISHED = 3
    id = models.AutoField(primary_key=True, unique=True)
    contenido = models.ForeignKey(Content)
    tipo_subasta = models.ForeignKey(TipoSubasta)
    # activa = models.BooleanField(default=True)
    fecha_inicio = models.DateTimeField(blank=True)
    tiempo_regresivo = models.TimeField()
    fecha_expiracion = models.DateTimeField(blank=True, editable=False, null=True)
    # precio_minimo = models.FloatField()
    precio_actual = models.FloatField(editable=False)
    gana_robot = models.BooleanField(default=True)
    membresia_minima = models.ForeignKey(TipoMembresia, null=True)
    # state for subasta
    # 1 waiting, 2 active, 3 finished
    estado = models.IntegerField(default=1, editable=False)
    ganador = models.ForeignKey(User, default=None, editable=False, null=True)

    def save(self, raw=False, force_insert=False,
             force_update=False, using=None, update_fields=None):
        if self.id is None and self.fecha_expiracion is None:
            # print "Updating Subasta **************************** fecha expiracion"
            tiempo_expiracion = timedelta(hours=self.tiempo_regresivo.hour, minutes=self.tiempo_regresivo.minute,
                                          seconds=self.tiempo_regresivo.second)
            self.fecha_expiracion = self.fecha_inicio + tiempo_expiracion
            if hasattr(self.contenido, 'articulo'):
                self.precio_actual = self.contenido.articulo.precio
            else:
                self.precio_actual = self.contenido.paquetebid.precio

        # ojo con la llamada al super
        super(Subasta, self).save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return "Subasta de %s" % self.contenido.nombre


class ShoppinggCart(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(User)


class SubastaVendida(models.Model):
    id = models.AutoField(primary_key=True)
    subasta = models.OneToOneField(Subasta)
    shoping_cart = models.ForeignKey(ShoppinggCart)


class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    subasta = models.OneToOneField(SubastaVendida, on_delete=models.CASCADE)
    a_usuario = models.IntegerField()
    precio = models.FloatField(null=False)
    fecha_creacion = models.DateTimeField(auto_now=True)
    en_red_de_usuario = models.ForeignKey(User)
    confirmada = models.BooleanField(default=False)
    fecha_confirmacion = models.DateTimeField(null=True)


class VentaArticulo(Venta):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)


class VentaPaqueteBid(Venta):
    paquete = models.ForeignKey(PaqueteBid, on_delete=models.CASCADE)


class Robot(models.Model):
    id_robot = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(User)
    subasta = models.OneToOneField(Subasta, null=True)

    class Meta:
        db_table = 'robots'

    def __str__(self):
        return self.nick


class AutoPuja(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User)
    cantidad_pujas = models.IntegerField(default=1)
    articulo = models.ForeignKey(to=Articulo)

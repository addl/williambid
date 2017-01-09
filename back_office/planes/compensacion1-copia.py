from back_office.banco import depositar_monto_en_cuenta_de_usuario
from back_office.models import TipoMembresia
from back_office.util import obtener_total_ventas_de_articulo_de_miembro, obtener_total_ventas_de_paquetes_de_miembro

__author__ = 'bryan'

from django.contrib.auth.models import User


class PlanCompensacionUno():
    """Aun falta ver lo de las posiciones 2,4,6,10,15, 20,......"""

    def __init__(self, arbol_general):
        self.NUMERO_PLAN = 1
        self.arbol_general = arbol_general


    def asignar_ganancia_a_cada_usuario(self):
        # recorrido del arbol
        mapa = {}
        self.arbol_general.obtener_ganancia_por_nodo(mapa)
        for miembro_id, ganancia in mapa:
            monto_de_usuario = self.calcular_monto_total_de_usuario(miembro_id, ganancia)
            depositar_monto_en_cuenta_de_usuario(miembro_id, monto_de_usuario, self.NUMERO_PLAN)

    def calcular_monto_total_de_usuario(self, miembro_id, ganancia):
        tipo_membresia = User.objects.get(id=miembro_id).perfilusuario.membresia.tipo_membresia
        total_venta_de_la_red = self.obtener_total_ventas_de_la_red_de(miembro_id)
        # membresia FREE
        if tipo_membresia.id == 1:
            return self.obtener_x_porciento_de(total_venta_de_la_red, 10)
        # para las otras membresias
        total_venta_de_red_de_tu_membresia = self.obtener_total_ventas_de_la_red_de_membresia(miembro_id,
                                                                                              tipo_membresia.id)
        # membresia BASIC
        if tipo_membresia.id == 2:
            return self.calcular_valor_ventas(total_venta_de_red_de_tu_membresia, 50, miembro_id, tipo_membresia.id, 25)
        # membresia BRONCE
        if tipo_membresia.id == 3:
            return self.calcular_valor_ventas(total_venta_de_red_de_tu_membresia, 50, miembro_id, tipo_membresia.id, 30)
        # membresia PLATA
        if tipo_membresia.id == 4:
            return self.calcular_valor_ventas(total_venta_de_red_de_tu_membresia, 50, miembro_id, tipo_membresia.id, 35)
        # membresia ORO
        if tipo_membresia.id == 5:
            return self.calcular_valor_ventas(total_venta_de_red_de_tu_membresia, 50, miembro_id, tipo_membresia.id, 40)
        # membresia PLATINO
        if tipo_membresia.id == 6:
            return self.calcular_valor_ventas(total_venta_de_red_de_tu_membresia, 50, miembro_id, tipo_membresia.id, 45)
        # membresia DIAMANTE
        if tipo_membresia.id == 7:
            return self.calcular_valor_ventas(total_venta_de_red_de_tu_membresia, 50, miembro_id, tipo_membresia.id, 50)
        # membresia VIP
        if tipo_membresia.id == 8:
            return self.calcular_valor_ventas(total_venta_de_red_de_tu_membresia, 50, miembro_id, tipo_membresia.id, 50)
        # membresia VIP-PRO
        if tipo_membresia.id == 9:
            return self.obtener_x_porciento_de(total_venta_de_la_red, 70)

    def calcular_valor_ventas(self, total_venta_membresia, x_ciento_mem, miembro_id, tipo_membresia_id,
                              x_ciento_paquete):
        ventas = self.obtener_x_porciento_de(total_venta_membresia, x_ciento_mem)
        ventas_paquetes = self.obtener_total_ventas_de_paquetes_bids_membresias_excepto(miembro_id, tipo_membresia_id)
        return ventas + self.obtener_x_porciento_de(ventas_paquetes, x_ciento_paquete)

    def obtener_x_porciento_de(self, monto, porciento):
        return float(monto * porciento / 100)


    def calcular_monto_por_ser_proveedor(self, miembro_id):
        lista = self.obtener_red_de_proveedor_para(miembro_id)
        suma = 0
        for miembro in lista:
            suma += self.cal


    def obtener_total_ventas_de_la_red_de(self, miembro_id):
        red = self.obtener_red_del_miembro(miembro_id)
        ventas_de_la_red = 0
        for miembro in red:
            ventas_de_la_red += obtener_total_ventas_de_articulo_de_miembro(miembro)
        return ventas_de_la_red

    def obtener_total_ventas_de_la_red_de_membresia(self, miembro_id, tipo_membresia_id):
        red = self.obtener_red_del_miembro(miembro_id)
        tipo_membresia = TipoMembresia.objects.get(id=tipo_membresia_id)
        ventas_de_la_red = 0
        for miembro in red:
            usuario_miembro = User.objects.get(id=miembro)
            if usuario_miembro.perfilusuario.membresia.tipo_membresia == tipo_membresia:
                ventas_de_la_red += obtener_total_ventas_de_articulo_de_miembro(miembro)
        return ventas_de_la_red

    def obtener_total_ventas_de_paquetes_bids_membresias_excepto(self, miembro_id, tipo_membresia_no_cuenta_id):
        red = self.obtener_red_del_miembro(miembro_id)
        tipo_membresia = TipoMembresia.objects.get(id=tipo_membresia_no_cuenta_id)
        ventas_de_la_red = 0
        for miembro in red:
            usuario_miembro = User.objects.get(id=miembro)
            if usuario_miembro.perfilusuario.membresia.tipo_membresia != tipo_membresia:
                ventas_de_la_red += obtener_total_ventas_de_paquetes_de_miembro(miembro)
        return ventas_de_la_red


    def obtener_red_del_miembro(self, miembro_id):
        # devolvera la lista de enteros(IDs) de los miembros hijos de miembro_id
        red = []
        hijos = self.arbol_general.obtener_hijos_de(miembro_id)
        cant = len(hijos)
        if cant > 1:
            for i in range(1, cant + 1):
                if i != 2 and i != 4 and i != 6:
                    if i == 5:
                        red.append(hijos[i - 1])
                    elif i % 5 != 0:
                        red.append(hijos[i - 1])


    def obtener_red_de_proveedor_para(self, miembro_id):
        return self.arbol_general.obtener_arbol_de_raiz(miembro_id).obtener_hijos_proveedor()
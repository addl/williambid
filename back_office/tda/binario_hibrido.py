from back_office.banco import obtener_factura_total_de_usuario, depositar_monto_en_cuenta_de_usuario
from back_office.util import obtener_comision_para_usuario, obtener_x_porciento_de

__author__ = 'bryan'

# no definimos herencia pq estaria incompleto toda la arquitectura, o sea hay que definir todos los tda de arbol
# mantenemos cada uno aparte, no hay tiempo para implementarlos todos

class ArbolBinarioHibrido():
    def __init__(self, raiz=None, izquierdo=None, derecho=None):
        self.raiz = raiz
        self.izquierdo = izquierdo
        self.derecho = derecho
        self.__adicionar_a_la_izquierda = True


    # este metodo se corresponde con el plan de compensacion 2
    # entiendo que el dinero q se maneja es la factura total de los usuarios

    def evaluar_arbol(self, mapa_resultados):
        mi_factura = obtener_factura_total_de_usuario(self.raiz, except_plan=2)
        if self.es_hoja():
            return mi_factura
        suma_izq = self.izquierdo.evaluar_arbol(mapa_resultados) if self.izquierdo else 0.0
        suma_der = self.derecho.evaluar_arbol(mapa_resultados) if self.derecho else 0.0
        # si tiene ambos hijos, es un requisito para cobrar, then factura por ambos lados, hay q calcular
        if self.derecho and self.izquierdo:
            menor_factura = min(suma_izq, suma_der)
            por_ciento_de_comision = obtener_comision_para_usuario(self.raiz)
            cantidad_recibida = obtener_x_porciento_de(menor_factura, por_ciento_de_comision)
            mapa_resultados[self.raiz.id] = cantidad_recibida
        # retornar lo que evalue en mi arbol completo
        return mi_factura + suma_izq + suma_der

    def adicionar_usuario(self, usuario_nuevo, usuario_padre):
        arbol_padre = self.__buscar_a_lo_ancho(usuario_padre)
        arbol_padre.__adicionar_sub_arbol(ArbolBinarioHibrido(usuario_nuevo))

    def __buscar_a_lo_ancho(self, raiz_usuario):
        if self.raiz == raiz_usuario:
            return self
        cola = list()
        cola.append(self)
        while len(cola) > 0:
            frente = cola.__getitem__(0)
            cola.remove(frente)
            if frente.raiz == raiz_usuario:
                return frente
            else:
                if frente.izquierdo:
                    cola.append(frente.izquierdo)
                if frente.derecho:
                    cola.append(frente.derecho)
        return None

    def __adicionar_sub_arbol(self, sub_arbol):
        if self.es_hoja():
            self.izquierdo = sub_arbol
            self.__adicionar_a_la_izquierda = False
        else:
            if self.__adicionar_a_la_izquierda:
                self.__adicionar_a_la_izquierda = False
                if self.izquierdo:
                    self.izquierdo.__acomodar_arbol_a_la_izquierda(sub_arbol)
                else:
                    self.izquierdo = sub_arbol
            else:
                self.__adicionar_a_la_izquierda = True
                if self.derecho:
                    self.derecho.__acomodar_arbol_a_la_derecha(sub_arbol)
                else:
                    self.derecho = sub_arbol


    def __acomodar_arbol_a_la_izquierda(self, sub_arbol):
        if self.izquierdo:
            self.izquierdo.__acomodar_arbol_a_la_izquierda(sub_arbol)
        else:
            self.izquierdo = sub_arbol

    def __acomodar_arbol_a_la_derecha(self, sub_arbol):
        if self.derecho:
            self.derecho.__acomodar_arbol_a_la_derecha(sub_arbol)
        else:
            self.derecho = sub_arbol


    def es_hoja(self):
        return not self.izquierdo and not self.derecho
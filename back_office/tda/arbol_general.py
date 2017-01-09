from django.contrib.auth.models import User

from back_office.util import obtener_x_porciento_de, obtener_total_ventas_de_paquetes_de_miembro

__author__ = 'bryan'


class ArbolGeneral():
    raiz = None
    lista_subarboles = []

    def __init__(self, raiz):
        self.raiz = raiz
        self.lista_subarboles = []

    def adicionar_subarbol_hijo(self, arbol):
        if not isinstance(arbol, ArbolGeneral):
            raise Exception("Arbol general solo puede adicionar ArbolGeneral.")
        self.lista_subarboles.append(arbol)
        return True


    # esta funcion responde a las ganancias del plan de compensacion 1
    # responde a la ventas de paquetes
    # debe de repartirse mensualmente
    def obtener_ganancia_por_nodo(self, map, proveedor=None):
        usuario = self.raiz
        ganancia_neta = obtener_total_ventas_de_paquetes_de_miembro(usuario.id)
        ganancia_proveedor = 0.0
        mi_proveedor = proveedor
        # for v in ventas_pktes:
        #     ganancia_neta += v.precio

        if self.es_hoja():
            return ganancia_neta
        else:
            subarboles = self.lista_subarboles
            cant_hijos = len(subarboles)
            for i in range(1, cant_hijos + 1):
                sub_arbol = subarboles[i - 1]
                if (i == 2 or i == 4 or i == 6) or (i > 9 and i % 5 == 0):
                    ingresos_nodo = sub_arbol.obtener_ganancia_por_nodo(map, self)
                    if mi_proveedor:
                        ganancia_proveedor += self.calcular_monto_total_de_usuario(mi_proveedor.raiz, ingresos_nodo)
                else:
                    ingresos_nodo = sub_arbol.obtener_ganancia_por_nodo(map, self)
                    ganancia_neta += self.calcular_monto_total_de_usuario(usuario, ingresos_nodo)

        if map.__contains__(usuario.id):
            suma = map.get(usuario.id) + ganancia_neta
            map[usuario.id] = suma
        else:
            map[usuario.id] = ganancia_neta

        if mi_proveedor:
            id_p = mi_proveedor.raiz.id
            if map.__contains__(id_p):
                suma = map.get(id_p) + ganancia_proveedor
                map[id_p] = suma
            else:
                map[proveedor.raiz.id] = ganancia_proveedor
        return ganancia_neta


    def calcular_monto_total_de_usuario(self, usuario, ingresos):
        tipo_membresia = usuario.perfilusuario.membresia.tipo_membresia
        # membresia FREE
        if tipo_membresia.id == 1:
            return obtener_x_porciento_de(ingresos, 10)
        # membresia BASIC
        if tipo_membresia.id == 2:
            return obtener_x_porciento_de(ingresos, 25)
        # membresia BRONCE
        if tipo_membresia.id == 3:
            return obtener_x_porciento_de(ingresos, 30)
        # membresia PLATA
        if tipo_membresia.id == 4:
            return obtener_x_porciento_de(ingresos, 35)
        # membresia ORO
        if tipo_membresia.id == 5:
            return obtener_x_porciento_de(ingresos, 40)
        # membresia PLATINO
        if tipo_membresia.id == 6:
            return obtener_x_porciento_de(ingresos, 45)
        # membresia DIAMANTE
        if tipo_membresia.id == 7:
            return obtener_x_porciento_de(ingresos, 50)
        # membresia VIP
        if tipo_membresia.id == 8:
            return obtener_x_porciento_de(ingresos, 50)
        # membresia VIP-PRO
        if tipo_membresia.id == 9:
            return obtener_x_porciento_de(ingresos, 50)

    def adicionar_subarbol(self, arbol_padre, arbol_hijo):
        if self.raiz == arbol_padre.raiz:
            return self.adicionar_subarbol_hijo(arbol_hijo)
        else:
            nodo = self.buscar_arbol(arbol_padre)
            if nodo:
                return nodo.adicionar_subarbol_hijo(arbol_hijo)
            else:
                raise Exception("El elemento padre no existe en el arbol")
        return False


    def obtener_hijos_proveedor(self):
        """Devuelve una lista de los elementos raiz de cada uno de sus hijos"""
        res = []
        for arbol in self.lista_subarboles:
            raiz_sub_arbol = arbol.raiz
            hijos_subarbol = self.obtener_hijos_de(raiz_sub_arbol)
            cant = len(hijos_subarbol)
            if cant > 1:
                for i in range(1, cant + 1):  # recorremos con uno mas para mantener los numeros multiplos de 5
                    if i == 2 or i == 4 or i == 6:
                        res.append(hijos_subarbol[i - 1])
                    elif i > 6 and i % 5 == 0:
                        res.append(hijos_subarbol[i - 1])
        print "Los hijos de %s son %s" % (self.raiz, res)
        return res

    def obtener_arbol_de_raiz(self, raiz):
        if self.raiz == raiz:
            return self
        else:
            result = None
            for sub_arbol in self.lista_subarboles:
                result = sub_arbol.obtener_arbol_de_raiz(raiz)
                if result:
                    return result
        return None

    def recorrer_a_lo_ancho(self):
        """
            Retorna una lista de todos los miembros a lo ancho, cada elemento contiene la el id de los miembros
        """
        cola = []
        recorrido = []
        cola.append(self)
        while len(cola) > 0:
            frente = cola.__getitem__(0)
            cola.remove(frente)
            recorrido.append(frente.raiz)
            for sub_arbol in frente.lista_subarboles:
                cola.append(sub_arbol)
        return recorrido


    def buscar_arbol(self, sub_arbol):
        """
        Recibe en arbol
        Devuelve el arbol cuya raiz se la pasada por parametro
        """
        if self.raiz == sub_arbol.raiz:
            return self
        else:
            result = None
            for arbol in self.lista_subarboles:
                result = arbol.buscar_arbol(sub_arbol)
                if result:
                    return result
        return None



    def obtener_primera_generacion_de(self, id_user):
        result = list()
        sub_arbol = self.buscar_arbol(ArbolGeneral(User.objects.get(id=id_user)))
        if sub_arbol is None:
            #raise Exception("The specified parent was not found. No first generation returned")
            return result
        for arbol in sub_arbol.lista_subarboles:
            result.append(arbol.raiz)
        print("Returning first generation for %s" % id_user)
        return result

    def obtener_subarbol(self, pos):
        return self.lista_subarboles[pos]

    def grado(self):
        return len(self.lista_subarboles)

    def podar_subarbol(self, pos):
        self.lista_subarboles.remove(pos)

    def es_hoja(self):
        return len(self.lista_subarboles) == 0

    def altura(self):
        if self.es_hoja():
            return 0
        else:
            mayor = 0
            for arbol in self.lista_subarboles:
                sub_a = arbol.altura() + 1
                if sub_a > mayor:
                    mayor = sub_a
            return mayor

    def __str__(self):
        return "Node: %s - Mem: %s - UserKind: %s" % \
               (self.raiz, self.raiz.perfilusuario.membresia.tipo_membresia_id, self.raiz.perfilusuario.tipo_usuario_id)
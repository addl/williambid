from django.contrib.auth.models import User

__author__ = 'bryan'


class ArbolHeap():
    def __init__(self, raiz=None, izquierdo=None, derecho=None):
        self.raiz = raiz
        self.izquierdo = izquierdo
        self.derecho = derecho


    # este metdo se corresponde con el plan de compensacion 4
    # se le otorga 0.2
    def evaluar_arbol(self, map_user_monto):
        total = 0.0
        if self.es_hoja():
            total = 0.2
        if self.izquierdo:
            total += self.izquierdo.evaluar_arbol(map_user_monto)
        if self.derecho:
            total += self.derecho.evaluar_arbol(map_user_monto)
        # print 'Nodo %s con %s' % (self.raiz, total)
        user = User.objects.get(id=self.raiz)
        if user.perfilusuario.tipo_usuario > 1:
            map_user_monto[self.raiz] = total
        return total


    def buscar_elemento(self, elemento):
        if self.es_hoja():
            if self.raiz == elemento:
                return self
            else:
                return None
        if self.raiz == elemento:
            return self
        else:
            elem = None
            if self.izquierdo:
                elem = self.izquierdo.buscar_elemento(elemento)
            if elem is None and self.derecho:
                return self.derecho.buscar_elemento(elemento)
        return None

    def es_hoja(self):
        return not self.izquierdo and not self.derecho


    def __str__(self):
        u = User.objects.get(id=self.raiz)
        return "Usuario: %s - Mem: %s - UserKind: %s" % (u.username, u.perfilusuario.membresia_id, u.perfilusuario.tipo_usuario_id)
__author__ = 'bryan'

from back_office.tda.arbol_general import ArbolGeneral

a = ArbolGeneral(1)
b = ArbolGeneral(2)
c = ArbolGeneral(3)

a.adicionar_subarbol_hijo(b)
a.adicionar_subarbol_hijo(c)
a.adicionar_subarbol_hijo(ArbolGeneral(10))

a.buscar_arbol(2).adicionar_subarbol_hijo(ArbolGeneral(6))
a.buscar_arbol(3).adicionar_subarbol_hijo(ArbolGeneral(4))
a.buscar_arbol(3).adicionar_subarbol_hijo(ArbolGeneral(5))

a.buscar_arbol(4).adicionar_subarbol_hijo(ArbolGeneral(8))
a.buscar_arbol(4).adicionar_subarbol_hijo(ArbolGeneral(9))

recorrido = a.recorrer_a_lo_ancho()
for node in recorrido:
    print node

print "Hijos de a %s " % a.obtener_hijos_de(1)
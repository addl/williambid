__author__ = 'bryan'
import os

import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "william.settings")

django.setup()

from back_office.tda.heap import ArbolHeap

if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6]
    a = ArbolHeap()
    a = a.construir_arbol(lista, 0)
    a.evaluar_arbol()
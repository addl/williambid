import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "william.settings")
django.setup()

from django.contrib.auth.models import User

from back_office.planes.compensacion5 import PlanCompensacionCinco
from back_office.planes.manager_planes import PlanesManagerSingleton

__author__ = 'bryan'


def test_tipo_reto_1():
    # probar tipo reto 1, okokokok
    user_nuevo = User.objects.get(id=5)
    user_padre = User.objects.get(id=2)
    PlanCompensacionCinco.computar_registro_de_usuario(user_nuevo, user_padre)
    plan_manager = PlanesManagerSingleton.get_instance()
    plan_manager.plan_compensacion_cinco.cerrar_retos_vencidos_por_fecha()


def test_tipo_reto_2():
    # probar tipo reto 2, okokokok
    user_con_new_mem = User.objects.get(id=5)
    PlanCompensacionCinco.computar_cambio_de_membresia(user_con_new_mem)
    plan_manager = PlanesManagerSingleton.get_instance()
    plan_manager.plan_compensacion_cinco.cerrar_retos_vencidos_por_fecha()


if __name__ == '__main__':
    test_tipo_reto_2()
    print "END EXECUTION"
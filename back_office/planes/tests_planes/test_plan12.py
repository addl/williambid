import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "william.settings")
django.setup()

from django.contrib.auth.models import User

from back_office.planes.manager_planes import PlanesManagerSingleton

__author__ = 'bryan'


def test_depositar_dinero():
    plan_manager = PlanesManagerSingleton.get_instance()
    plan_manager.plan_compensacion_doce_trece_catorce.evaluar_usuarios()


if __name__ == '__main__':
    test_depositar_dinero()
    print "END EXECUTION"
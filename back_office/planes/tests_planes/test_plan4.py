import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "william.settings")
django.setup()


from back_office.planes.manager_planes import PlanesManagerSingleton

__author__ = 'bryan'


if __name__ == '__main__':
    plan_manager = PlanesManagerSingleton.get_instance()
    plan_manager.plan_compensacion_cuatro.asignar_ganancia_a_usuarios()
    print "END EXECUTION"
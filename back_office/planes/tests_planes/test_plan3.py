import os
import django

from back_office.planes.manager_planes import PlanesManagerSingleton

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "william.settings")

django.setup()

from back_office.planes.compensacion4 import PlanCompensacionCuatro

if __name__ == '__main__':
    plan_manager = PlanesManagerSingleton.get_instance()
    plan_manager.plan_compensacion_tres.evaluar_usuarios()
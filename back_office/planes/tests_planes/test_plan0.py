import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "william.settings")
django.setup()

from back_office.planes.manager_planes import PlanesManagerSingleton



from williambid.service_layer import crear_usuario_para_robot

if __name__ == '__main__':
    plan_manager = PlanesManagerSingleton.get_instance()
    list = plan_manager.arbol_general.obtener_primera_generacion_de(1)
    print "First generation of admin: %s" % list
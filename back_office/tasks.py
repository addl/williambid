from __future__ import absolute_import

from william.celery_config import app

from back_office.planes.manager_planes import PlanesManagerSingleton
import logging

log = logging.getLogger(__name__)

manager_planes = PlanesManagerSingleton.get_instance()

# corre cada un minuto,
# debe correr cada un mes, una vez al mes
@app.task
def run_plans_manager():
    log.info("Running PlansManager with instance: %s " % manager_planes)
    manager_planes.execute_tasks()


# corre cada 10 seconds
@app.task
def run_short_periodical_tasks():
    #manager_planes = PlanesManagerSingleton.get_instance()
    log.info("Running PlansManager with instance: %s " % manager_planes)
    manager_planes.plan_compensacion_cinco.cerrar_retos_vencidos_por_fecha()


# Tareas relacionadas al plan 0, se llaman periodicamente para mostrar datos actualizados
# corren cada 1 hora
@app.task
def run_plan_zero_task():
    # actualizar la puntuacion de los usuarios
    manager_planes.plan_compensacion_general.actualizar_puntacion_de_usuarios()
    # actualizar el tipo de usuario de todos los usuarios antes de repartir las ganancias
    manager_planes.plan_compensacion_general.actualizar_tipo_usuario_para_cada_usuario()

# tareas que son necesarias intercambiar con redis, para obtener resultado de los planes
@app.task
def obtener_primera_generacion_de(user_id):
    log.info("Searching first generation for user_id: %s " % user_id)
    return manager_planes.arbol_general.obtener_primera_generacion_de(user_id)


@app.task
def registrar_usuario_nuevo_a_planes_de_compensacion(user_nuevo, user_padre):
    log.info("Registering nuevo usuario: %s a los planes de compensacion" % user_nuevo)
    manager_planes.registrar_usuario_a_planes_de_compensacion(user_nuevo, user_padre)


@app.task
def run_daily_tasks():
    # cambiar el tipo de membresia automaticamente segun los ingresos
    # mas info en el plan de compensacion 11 ONCE
    manager_planes.plan_compensacion_once.analizar_membresias_de_todos_los_usuarios()
    # chequear si los usuarios logran cumplir el plan de compensacion 10
    # mas info en el archivo de este plan
    manager_planes.plan_compensacion_diez.evaluar_usuarios()
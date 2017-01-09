from __future__ import absolute_import
from william.celery_config import app
from williambid.sincronizador import SincronizadorSingleInstance
#import logging

#log = logging.getLogger(__name__)
synchronizer = SincronizadorSingleInstance.get_instance()


@app.task
def run_synchronizer():
    synchronizer.execute_tasks()


@app.task
def run_synchronizer_main_task():
    synchronizer.verificar_subastas_terminadas()
    # aggregamos el chequeo de las autopujas
    synchronizer.autopujar_subastas()


@app.task
def asignar_robots_a_subastas(subasta_id):
    synchronizer.asignar_robots_a_subastas(subasta_id=subasta_id)

import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "william.settings")
django.setup()

from williambid.sincronizador import SincronizadorSingleInstance

sync = SincronizadorSingleInstance.get_instance()

sync.verificar_subastas_terminadas()

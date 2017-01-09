from __future__ import absolute_import

#import os

#os.environ['DJANGO_SETTINGS_MODULE'] = 'william.settings'


from celery import Celery

from datetime import timedelta

from williambid.sincronizador import SincronizadorSingleInstance

sincronizador = SincronizadorSingleInstance.get_instance()

app = Celery('william',
             broker='redis://localhost:6379',
             backend='redis://localhost:6379',
             include=['william.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
    CELERY_TASK_SERIALIZER='json',
    CELERY_ACCEPT_CONTENT=['json'],  # Ignore other content
    CELERY_RESULT_SERIALIZER='json',
    CELERY_TIMEZONE='America/New_York',
    CELERY_ENABLE_UTC=True,
    CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
        'task': 'william.tasks.myprint',
        'schedule': timedelta(seconds=30),
        'args': (sincronizador)
    },
}
)

if __name__ == '__main__':
    app.start()

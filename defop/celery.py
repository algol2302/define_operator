from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from celery.schedules import crontab


CELERYD_CONCURRENCY = 10

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'defop.settings')

app = Celery('defop')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.update(
    worker_max_tasks_per_child=1,
    broker_pool_limit=None
)

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'start_download': {
        'task': 'core.tasks.start_download',
        'schedule': crontab(
            hour=1, minute=0
        ),
    },
}

app.conf.timezone = os.environ.get('TIMEZONE', 'Asia/Krasnoyarsk')

import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flind_core.settings')

app = Celery('flind_core')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.result_backend = 'db+'+os.getenv("DATABASE_URL", "")

app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

web: gunicorn flind_core.wsgi --log-file -
celery: celery -A flind_core.celery worker -l info -c 4
celerybeat: celery -A flind_core.celery beat -l info
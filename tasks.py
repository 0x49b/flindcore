from celery import Celery

app = Celery('tasks', broker='pyamqp://guets@localhost')


@app.task
def add(x: int, y: int) -> int:
    return x + y

from celery import Celery

app = Celery('task', broker='pyamqp://admin:admin@localhost')

@app.task
def add(x, y):
    return x + y
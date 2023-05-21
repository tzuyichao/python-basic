from celery import Celery
from celery.utils.log import get_task_logger

app = Celery('tasks', broker='redis://localhost:6379/0', backend="redis://localhost:6379/1")

app.conf.update(
    result_expires=300,
)

logger = get_task_logger(__name__)

@app.task
def add(x, y):
    logger.info('Adding {0} + {1}'.format(x, y))
    return x + y

if __name__ == '__main__':
    app.start(["worker"])
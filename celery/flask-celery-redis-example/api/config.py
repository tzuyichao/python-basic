class FlaskConfig():
    SERVER_SLEEP = 10

class CeleryConfig():
    CELERY_BROKER_URL = "redis://redis:6379/0"
    CELERY_RESULT_BACKEND = "redis://redis:6379/0"
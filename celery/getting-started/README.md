
```bash=
docker run -d -p 5672:5672 rabbitmq

docker run -d -p 6379:6379 redis

celery -A tasks worker --loglevel=INFO

celery -A tasks worker -E --loglevel=INFO
```

```bash=
from tasks import add
add.run(3, 3)

r = add.apply_async((10, 10), expires=1)

r.ready()

r.get(timeout=10)
```

[Celery + Redis](https://riptutorial.com/celery/example/23628/celery-plus-redis)


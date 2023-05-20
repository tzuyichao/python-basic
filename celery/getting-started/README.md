
```bash=
docker run -d --name activemq -p 5672:5672 -p 61616:61616 -p 8161:8161 webcenter/activemq

celery -A tasks worker --loglevel=INFO
```

```bash=

```


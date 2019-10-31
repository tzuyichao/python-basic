# https://sdiehl.github.io/gevent-tutorial/
import gevent
from gevent.queue import Queue

tasks = Queue()

def worker(n):
    while not tasks.empty():
        task = tasks.get()
        print('Worker %s got task %s' % (n, task))
        gevent.sleep(0)
    print('Quiting time!')

def boss():
    for i in range(1, 25):
        tasks.put_nowait(i)
    print('Completed')

print('before boss running')
gevent.spawn(boss).join()
print('after boss running')

gevent.joinall([
    gevent.spawn(worker, 'steve'),
    gevent.spawn(worker, 'john'),
    gevent.spawn(worker, 'nancy'),
])
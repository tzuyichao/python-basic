from gevent import monkey
monkey.patch_all()
from flask import Flask
import gevent
from gevent.queue import Queue
from gevent import Greenlet
import time
import signal
import sys

class Actor(gevent.Greenlet):

    def __init__(self):
        self.inbox = Queue()
        Greenlet.__init__(self)

    def receive(self, message):
        """
        Define in your subclass.
        """
        raise NotImplemented()

    def _run(self):
        self.running = True

        while self.running:
            message = self.inbox.get()
            self.receive(message)

class Logger(Actor):
    def receive(self, message):
        gevent.sleep(2)
        f= open("./test.txt","a+")
        f.write("%s: %s\n" % (time.ctime(), message))
        f.close()
        

app = Flask(__name__)

logger = Logger()
logger.start()

def exist_handler(signalNumber, frame):
    print(logger)
    logger.running = False
    sys.exit(0)

signal.signal(signal.SIGINT, exist_handler)
signal.signal(signal.SIGTERM, exist_handler)

@app.route('/hello')
def helloIndex():
    print("%s: %s\n" % (time.ctime(), 'before'))
    logger.inbox.put('hello called')
    print("%s: %s\n" % (time.ctime(), 'after'))
    return 'Hello World from Python Flask!'

app.run(host='0.0.0.0', port= 5000)
import gevent
import time

def logging():
    f= open("./test.txt","w+")
    f.write('test')
    gevent.sleep(3)
    f.close()

# print("Start : %s" % time.ctime())
# logging()
# print("End : %s" % time.ctime())

print("Start : %s" % time.ctime())
gevent.spawn(logging).join()
print("End : %s" % time.ctime())

time.sleep(10)

print('all done.')
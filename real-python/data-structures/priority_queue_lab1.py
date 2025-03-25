import threading, queue, time

source = ['2-吃飯', '1-睡覺', '3-寫程式', '7-散步', '5-聽音樂', '6-看書', '4-玩電動']
threads_num = 3

q = queue.PriorityQueue()
for item in source:
    q.put(item)

def worker():
    print("Worker start")
    while True:
        item = q.get()
        if item == 'STOP':
            print("Worker stop")
            break
        print("Processing", item)
        time.sleep(0.01)
        q.task_done()

threads = []
for _ in range(threads_num):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

q.join()

for _ in range(threads_num):
    q.put('STOP')

for t in threads:
    t.join()
print("All done")
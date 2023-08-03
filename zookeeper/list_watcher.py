from kazoo.client import KazooClient

def watch_children(children):
    print(f"Children of the node: {children}")

def print_watcher(zk):
    try:
        zk.start()

        zk.get_children("/brokers/topics/test.topic.v0", watch=watch_children)
        while True:
            pass
    except Exception as e:
        print(f"Error: {e}")

    finally:
        zk.stop()
        zk.close()

if __name__ == "__main__":
    zk_host = "localhost:2181"

    zk = KazooClient(hosts=zk_host)

    print_watcher(zk)

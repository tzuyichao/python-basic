from kazoo.client import KazooClient
import logging

logging.basicConfig(level=logging.DEBUG)
zk_host = "localhost:2181"
zk = KazooClient(hosts=zk_host, use_ssl=False, read_only=True)

zk.start()
zk.stop()
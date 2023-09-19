import sys
import time
import random
import threading
from confluent_kafka import Producer

bootstrap_servers = "10.0.0.5:9092"
topic = "test.topic"

def generate_random_string(size):
  characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" 
  return ''.join(random.choice(characters) for _ in range(size))

def produce_messages(id, producer, topic, message_size, num_messages):
  print(f"Thread: {id} started.")
  for i in range(num_messages):
    message = generate_random_string(message_size)
    producer.produce(topic, key=str(i), value=message)
    producer.flush()
    # print(f"Thread: {id} Produced message {i} size {len(message)}")
  print(f"Thread: {id} done.")

def main():
  if len(sys.argv) != 3:
    print("Usage: python multithread_message_produce.py <message_size> <num_messages>")
    sys.exit(1)

  message_size = int(sys.argv[1])
  num_messages = int(sys.argv[2])
  conf = {
    'bootstrap.servers': bootstrap_servers,
    'acks': 'all',
  }
  producer = Producer(conf)
  num_threads = 4
  threads = []
  id = 0
  for _ in range(num_threads):
    thread = threading.Thread(target=produce_messages, args=(id, producer, topic, message_size, num_messages))
    threads.append(thread)
    thread.start()
    id = id + 1
  for thread in threads:
    thread.join()

if __name__ == "__main__":
  main()

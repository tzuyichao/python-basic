from confluent_kafka import Consumer, KafkaError, KafkaException
import sys

if __name__ == '__main__':
    conf = {
        'bootstrap.servers': 'YOUR_KAFKA_BROKER:9093', 
        'security.protocol': 'SASL_PLAINTEXT',
        'sasl.mechanisms': 'SCRAM-SHA-512',
        'sasl.username': 'ACCOUNT', 
        'sasl.password': 'PASSWORD',
        'group.id': '<your_group_id>',
        'client.id': 'python_consumer'
    }

    consumer = Consumer(conf)
    running = True
    topic = 'test.testtopic.v0'
    running = True
    def basic_consume_loop(consumer, topics):
        try:
            consumer.subscribe(topics)

            while running:
                print("polling...")
                msg = consumer.poll(timeout=1.0)
                if msg is None: continue

                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        # End of partition event
                        sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                        (msg.topic(), msg.partition(), msg.offset()))
                    elif msg.error():
                        raise KafkaException(msg.error())
                else:
                    msg_process(msg)
        finally:
            # Close down consumer to commit final offsets.
            consumer.close()

    def shutdown():
        running = False
    
    def msg_process(msg):
        print(msg.value().decode('utf-8'))

    basic_consume_loop(consumer, topics=[topic])

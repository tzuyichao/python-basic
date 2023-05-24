from confluent_kafka import Producer
import time

if __name__ == '__main__':
    conf = {
        'bootstrap.servers': 'KAFKA_BROKER',  # 例如: 'localhost:9092'
        'security.protocol': 'SASL_PLAINTEXT',  # or 'SASL_SSL'
        'sasl.mechanisms': 'SCRAM-SHA-512',
        'sasl.username': 'ACCOUNT',  # 你的登入驗證名稱
        'sasl.password': 'PASSWD',  # 你的登入驗證密碼
        'group.id': '<your_group_id>',  # 你的 group id
        'client.id': 'python_producer'
    }
    producer = Producer(**conf)
    def delivery_callback(err, msg):
        if err:
            print(f"Message delivery failed: {err}")
        else:
            print(f"Message delivered to {msg.topic()} [{msg.partition()}]")
    key = "key1"
    value = "value1"
    producer.produce('test.testtopic.v0', key=key, value=value, callback=delivery_callback)
    producer.flush()
    print("Send...")
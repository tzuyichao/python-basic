from confluent_kafka import Producer
from dotenv import load_dotenv
import os
import sys

def delivery_callback(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [Partition: {msg.partition()}]")
        # Log the size of the sent message
        message_size = len(msg.value())
        message_obj_size = sys.getsizeof(msg)
        print(f"Sent message value size: {message_size} bytes")
        print(f"Sent message object size: {message_obj_size} bytes")
        print(f"message value: {msg.value()}")
        print(f"message: {msg}")

if __name__ == '__main__':
    load_dotenv('.env')
    kafka_bootstrap_servers = os.getenv('KAFKA_BOOTSTRAP_SERVER')
    kafka_account = os.getenv('KAFKA_ACCOUNT')
    kafka_password = os.getenv('KAFKA_PASSWORD')
    conf = {
        'bootstrap.servers': kafka_bootstrap_servers, 
        'security.protocol': 'SASL_PLAINTEXT',
        'sasl.mechanisms': 'SCRAM-SHA-512',
        'sasl.username': kafka_account, 
        'sasl.password': kafka_password,
        'group.id': '<your_group_id>',
        'client.id': 'python_producer'
    }
    producer = Producer(**conf)
            
    # key = """{
    #     \"schema\": {
    #         \"type\": \"struct\", 
    #         \"fields\": [ 
    #             {\"type\": \"string\", \"optional\": false, \"field\": \"DATAKEY\"} 
    #         ], 
    #         \"optional\": false 
    #     }, 
    #     \"payload\": { 
    #         \"DATAKEY\": \"2753031\" 
    #     } 
    # }"""
    # value = """{ 
    #     \"schema\": { 
    #             \"type\": \"struct\", 
    #             \"fields\": [
    #                 { \"type\": \"string\", \"optional\": false, \"field\": \"DATAKEY\" },
    #                 { \"type\": \"string\", \"optional\": true, \"field\": \"APPLY_FORM_NO\" },
    #                 { \"type\": \"string\", \"optional\": true, \"field\": \"DTPHBG\" } 
    #             ], 
    #             \"optional\": false 
    #     }, 
    #     \"payload\": {
    #         \"DATAKEY\": \"2753031\", 
    #         \"APPLY_FORM_NO\": \"PH-202300000113202300000113202300000113\", 
    #         \"DTPHBG\": \"5\"
    #     }
    # }"""
    # topic = 'test.datagov.db.table.v7'
    key = "1"
    value = "1"
    topic = "test.testtopic.v0"
    producer.produce(topic=topic, key=key, value=value, callback=delivery_callback)
    producer.flush()
    print("Send...")
from confluent_kafka.admin import AdminClient
from dotenv import load_dotenv
import os

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
    admin_client = AdminClient(conf)
    topics = admin_client.list_topics(timeout=10)
    for topic in topics.topics.values():
        print(f"{topic}")
        print("Partitions:")
        for partition in topic.partitions.values():
            print(f"  {partition}: {type(partition)}")
            print(f"    Replicas: {partition.replicas}")
            

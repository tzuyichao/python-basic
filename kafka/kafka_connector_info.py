from dotenv import load_dotenv
import os
import requests
import logging

logger = logging.getLogger(__name__)

class KafkaConnectorInfo:
    def __init__(self):
        load_dotenv('.env')
        self.connector_url = os.getenv('KAFKA_CONNECTOR_URL')
    
    def get_connector_cluster(self):
        url = f"{self.connector_url}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            logger.error(f"Error: {response.status_code}")
            return None
    
    def get_connector(self, connector_name):
        url = f"{self.connector_url}/connectors/{connector_name}/status"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            logger.error(f"Error: {response.status_code}")
            return None
    
    def list_connectors(self):
        url = f"{self.connector_url}/connectors"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            logger.error(f"Error: {response.status_code}")
            return None
    
    def delete_connector(self, connector_name):
        url = f"{self.connector_url}/connectors/{connector_name}"
        response = requests.delete(url)
        if response.status_code == 204:
            return True
        else:
            logger.error(f"Error: {response.status_code}")
            return False

if __name__ == '__main__':
    kafka_connector_info = KafkaConnectorInfo()
    connector_cluster = kafka_connector_info.get_connector_cluster()
    print(f"Cluster: {connector_cluster}")
    for connector in kafka_connector_info.list_connectors():
        connector_status = kafka_connector_info.get_connector(connector)
        print(f"connector: {connector}, status: {connector_status['connector']['state']}")
        # delete_flag = True
        for task in connector_status['tasks']:
            print(f"\ttask: {task['id']}, status: {task['state']}")
        #     if delete_flag == True and task['state'] == 'RUNNING':
        #         delete_flag = False
        # if delete_flag:
        #     print(f"==> Delete connector: {connector}")
        #     if kafka_connector_info.delete_connector(connector):
        #         print(f"====> Delete connector: {connector} successfully")
        #     else:
        #         print(f"====> Delete connector: {connector} failed")
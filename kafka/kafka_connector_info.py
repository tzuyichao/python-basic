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

if __name__ == '__main__':
    pass
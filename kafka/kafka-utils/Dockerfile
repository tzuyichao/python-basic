FROM python:latest

RUN apt update && apt upgrade -y
RUN apt install vim -y

RUN pip install kafka-utils

COPY ssh/sshconfig root/.ssh/config
COPY cluster_data/data_gov.yaml /etc/kafka_discovery/data_gov.yml


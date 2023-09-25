#!/bin/bash

if [[ ! -d ./ssh || ! -d ./cluster_data ]]; then
        echo "ssh or cluster_data folder does not exist."
	exit 1
fi

if [[ ! -f ./ssh/sshconfig ]]; then
	echo "sshconfig does not exist."
	exit 1
fi

if [[ ! -f ./cluster_data/data_gov.yaml ]]; then
	echo "cluster configuration does not exist."
	exit 1
fi

if [ "$#" -ne 2 ]; then
	echo "You need provide cluster name and ssh password"
	exit 1
fi

ENV=$1
PASSWORD=$2

JOLOKIA_PORT=9990
STOP_COMMAND="/var/lib/kfk-jolokia-stop.sh"
START_COMMAND="/var/lib/kfk-jolokia-start.sh"

sudo docker build . -t kafka-utils

sudo docker run --rm kafka-utils /bin/bash -c "kafka-rolling-restart --cluster-type data_gov --cluster-name $ENV --check-interval 30 --check-count 5 --jolokia-port $JOLOKIA_PORT --ssh-password $PASSWORD --stop-command $STOP_COMMAND --start-command $START_COMMAND"


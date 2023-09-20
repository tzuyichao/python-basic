#!/bin/bash

N=${1:-10}
IMAGE_NAME="producer"

sudo docker build . -t $IMAGE_NAME

for ((i=1; i<=N; i++)); do
	container_name="producer$i"
	sudo docker run -d --rm --name $container_name $IMAGE_NAME
done


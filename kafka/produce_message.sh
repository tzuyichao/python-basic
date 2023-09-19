#!/bin/bash

N=10

for ((i=1; i<=N; i++)); do
       tag_name="produce$i"
       sudo docker build . -t $tag_name
done

for ((i=1; i<=N; i++)); do
	tag_name="produce$i"
	sudo docker run -d $tag_name
done


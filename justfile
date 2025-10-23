# set dotenv-load

build:
    sudo docker build \
    --platform=linux/amd64 \
    --build-arg VORTEX_REPO=$VORTEX_REPO \
    -t vortex-develop \
    -f Dockerfile . 
    sudo docker create -p 2222:22 --name vortex-container vortex-develop

start:
    sudo docker start vortex-container

stop: 
    sudo docker stop vortex-container

enter:
    sudo docker start vortex-container
    sudo docker exec -it vortex-container /bin/bash

mount:
    sshfs -v -p 2222 root@localhost:/vortex ./vortex
    #password is vlsilab

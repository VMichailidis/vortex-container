build: 
    sudo docker build --platform=linux/amd64 -t vortex-ssh -f Dockerfile .

run:
    sudo docker run -d -p 2222:22 --name vortex-container vortex-ssh

stop: 
    sudo docker stop vortex-container

enter:
    sudo docker start vortex-container
    sudo docker exec -it vortex-container /bin/bash

mount:
    sshfs -v -p 2222 root@localhost:/vortex ./vortex
    #password is vlsilab

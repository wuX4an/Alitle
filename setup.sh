#!/bin/bash

#User information
whoami >> whoami

#Setup alitle command
chmod +x alitle
sudo cp alitle /bin

#Setup container
docker pull alpine:3.19
docker create -v /home/$USER/Alitle:/alitle --name alitle --network="host" -i alpine:3.19 /bin/ash
docker start alitle

#Share
docker cp whoami alitle:/
docker cp install.sh alitle:/
docker cp sshd_config alitle:/
docker exec alitle chmod +x install.sh
docker exec alitle ./install.sh

#remove shit
rm whoami
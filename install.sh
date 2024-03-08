#!/bin/bash

user=$(whoami)

cd /tmp
git clone https://github.com/wuX4an/Alitle
sleep 0.25
cd Alitle
sudo cp setups/base/ali /bin

sleep 0.25

mkdir /home/$user/.ali
mkdir /home/$user/.ali/bin/
mkdir /home/$user/.ali/conf/

sleep 0.25

cp ./setups/bin/* /home/$user/.ali/bin/
cp ./setups/conf/* /home/$user/.ali/conf/
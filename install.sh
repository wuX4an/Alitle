#!/bin/bash

cd /tmp
git clone https://github.com/wuX4an/Alitle.git >> ./shit
sleep 0.25
cd Alitle
sudo cp ./setups/ali /bin

mkdir /opt/ali/
mkdir /opt/ali/bin/
mkdir /opt/ali/conf/

cp ./setups/bin/* /opt/ali/bin/
cp ./setups/conf/* /opt/ali/conf/

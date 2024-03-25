#!/bin/bash

user=$(whoami)

cd /tmp
git clone https://github.com/wuX4an/Alitle
sleep 0.25
cd Alitle
chmod +x setups/base/ali
sudo cp setups/base/ali /bin

sleep 0.25

mkdir /home/$user/Alitle
mkdir /home/$user/Alitle/bin/
mkdir /home/$user/Alitle/conf/
mkdir /home/$user/Alitle/tools/

sleep 0.25

cp ./setups/bin/* /home/$user/Alitle/bin/
cp ./setups/conf/* /home/$user/Alitle/conf/
cp ./setups/tools/* /home/$user/Alitle/tools/
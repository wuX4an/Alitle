#!/bin/sh

# =============================================
#   CREATE .ali DIR
# =============================================
mkdir -p /home/$USER/.ali
mkdir -p /home/$USER/.ali/bin/
mkdir -p /home/$USER/.ali/conf/
mkdir -p /home/$USER/.ali/tools/

sleep 0.25

# =============================================
#   COPY THE DEPENDENCIES 
# =============================================
cp -r /tmp/Alitle/setups/bin/* /home/$USER/.ali/bin/
cp -r /tmp/Alitle/setups/conf/* /home/$USER/.ali/conf/
cp -r /tmp/Alitle/setups/tools/* /home/$USER/.ali/tools/
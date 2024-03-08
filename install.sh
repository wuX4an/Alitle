#!/bin/ash

#Install base
apk add curl wget git nano fish shadow sudo openssh-server openrc

#Install third party
wget https://raw.githubusercontent.com/dylanaraps/pfetch/master/pfetch
chmod +x pfetch
mv pfetch /bin

#Setup user
echo '%wheel ALL=(ALL) ALL' > /etc/sudoers.d/wheel
username=$(cat /whoami)
adduser -h alitle/$username -D $username
usermod -aG wheel $username
chown $username /alitle

#Setup shell
chsh root -s /usr/bin/fish
chsh $username -s /usr/bin/fish

#Setup ssh
mv sshd_config /etc/ssh
ssh-keygen -A
rc-status
touch /run/openrc/softlevel
/etc/init.d/sshd start

sleep 0.25

#Remove shits
rm whoami
rm install.sh

#Finishing
fish
echo -e "*****\033[32m Instalation Complete \033[0m*****"